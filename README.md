## Telavita Project Backend

### Running the API

To run this application, you will need Python 3+ and [Pipenv](https://pipenv.readthedocs.io/en/latest/) installed locally. If you have then, you can issue the following commands:

```bash
# from the flask-restful-apis directory
pipenv install
./bootstrap.sh
```

Then you can issue requests to your API. For example, with `curl`, you can issue requests like that:

```bash
# welcome page
curl http://localhost:5000/

# adding new employee
curl -X POST -H "Content-Type: application/json" -d '{"full_name": "Teste", "departament": "Administrativo", "dependents": 1}' http://localhost:5000/colaboradores

# listing all employees
curl http://localhost:5000/colaboradores

# listing all departaments
curl http://localhost:5000/departamentos
```
