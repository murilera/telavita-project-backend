import os
from config import db
from helpers import data, validate, responses
from models import colaborators, departaments


if os.path.exists('people.db'):
  os.remove('people.db')

db.drop_all()
db.create_all()

for c in data.colaboradores:
  p = colaborators.Colab(
    full_name=c['full_name'],
    departament=c['departament'],
    dependents=c['dependents']
  )
  db.session.add(p)

for d in data.departamentos:
  p = departaments.Departament(
    name = d
  )
  db.session.add(p)


db.session.commit()