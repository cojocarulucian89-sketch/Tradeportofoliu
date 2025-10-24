from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db, Portfolio
from ai_optimizer import recommend_portfolio

# Inițializare aplicație Flask
app = Flask(__name__)
CORS(app)

# Configurare conexiune SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tradeportofoliu.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# ✅ Rută principală pentru test backend (vizibilă și de pe Vercel)
@app.route("/")
def home():
    return jsonify({
        "message": "✅ NEWTRADE Pro AI Sentinel backend activ!",
        "status": "online"
    })

# ✅ Preluare active din baza de date
@app.route("/api/portfolio", methods=["GET"])
def get_portfolio():
    assets = Portfolio.query.all()
    return jsonify([a.to_dict() for a in assets])

# ✅ Adăugare activ nou
@app.route("/api/add", methods=["POST"])
def add_asset():
    try:
        data = request.get_json()
        new_item = Portfolio(symbol=data["symbol"], value=data["value"])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"status": "added", "asset": new_item.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# ✅ Optimizare portofoliu cu AI
@app.route("/api/optimize", methods=["POST"])
def optimize():
    data = request.get_json()
    suggestion = recommend_portfolio(data.get("assets", []))
    return jsonify(suggestion)

# ✅ Resetare completă a bazei de date
@app

