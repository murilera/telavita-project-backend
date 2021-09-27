from .. import db, ma


class Departament(db.Model):
    __tablename__ = 'departaments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class DepartamentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = Departament
        sqla_session = db.session
