from flask import current_app as app
from flask import Flask, render_template, jsonify, request
from .helpers import data, validate, responses
from .models import departaments
from .models import colaborators
from . import db

@app.route('/')
def home():
  return render_template('welcome.html')


@app.route('/departamentos')
def get_departamentos():
  d = departaments.Departament.query.all()
  departaments_schema = departaments.DepartamentSchema(many=True)
  return jsonify(departaments_schema.dump(d))


@app.route('/colaboradores')
def get_colaboradores():
  c = colaborators.Colab.query.all()
  colab_schema = colaborators.ColabSchema(many=True)
  colabs = colab_schema.dump(c)
  filtered = []
  
  for colab in colabs:
    colab['have_dependents'] = False
    if (colab['dependents'] > 0): colab['have_dependents'] = True
    filtered.append({key: value for key, value in colab.items() if key != 'dependents'})

  return jsonify(filtered)


@app.route('/colaboradores', methods=['POST'])
def add_colaboradores():
  colab = request.get_json()
  if (validate.is_valid_colab(colab)):
    full_name, departament, dependents = colab['full_name'], colab['departament'], colab['dependents']
    new_colab = colaborators.Colab(full_name=full_name, departament=departament, dependents=dependents)
    db.session.add(new_colab)
    db.session.commit()
    return responses.add_colab_success()
  return responses.add_colab_invalid()
