from .. import db, ma


class Colab(db.Model):
    __tablename__ = 'colabs'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    departament = db.Column(db.String(120), nullable=False)
    dependents = db.Column(db.Integer, nullable=False)

class ColabSchema(ma.Schema):
    class Meta:
        fields = ("full_name", "departament", "dependents")
        model = Colab
        sqla_session = db.session
