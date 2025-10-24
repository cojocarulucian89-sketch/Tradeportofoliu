from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    value = db.Column(db.Float)

    def to_dict(self):
        return {"id": self.id, "symbol": self.symbol, "value": self.value}
