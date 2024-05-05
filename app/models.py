from extensions import db

class Todo(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False) 
    done = db.Column(db.Boolean, default=False)
    important = db.Column(db.Boolean, default=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}