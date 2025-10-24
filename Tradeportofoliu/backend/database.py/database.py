from flask_sqlalchemy import SQLAlchemy

# Inițializare obiect SQLAlchemy (fără legare de aplicație)
db = SQLAlchemy()

# Model de tabel pentru portofoliu
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Conversie rapidă a obiectului SQLAlchemy la dicționar JSON."""
        return {
            "id": self.id,
            "symbol": self.symbol,
            "value": self.value
        }

# Funcție opțională pentru reinițializarea bazei (folosită doar la debug)
def init_db(app):
    """Creează tabelele dacă nu există deja."""
    with app.app_context():
        db.create_all()
