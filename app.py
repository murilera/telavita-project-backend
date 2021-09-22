from flask import Flask, render_template, jsonify, request

from . import data
from . import validate
from . import responses


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('welcome.html')


@app.route('/departamentos')
def departamentos():
  d = data.departamentos
  return jsonify(d)


@app.route('/colaboradores')
def get_colaboradores():
  c = data.colaboradores
  filtered = []
  
  for colab in c:
    colab['have_dependents'] = False
    if (colab['dependents'] > 0): colab['have_dependents'] = True
    filtered.append({key: value for key, value in colab.items() if key != 'dependents'})

  return jsonify(filtered)


@app.route('/colaboradores', methods=['POST'])
def add_colaboradores():
  colab = request.get_json()
  if (validate.is_valid_colab(colab)):
    data.colaboradores.append((request.get_json()))
    return responses.add_colab_success()
  return responses.add_colab_invalid()

if __name__ == '__main__':
  app.run(debug=True)
