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

# ✅ Rută principală test backend (verificare rapidă de pe Vercel)
@app.route("/")
def home():
    return jsonify({
        "message": "✅ NEWTRADE Pro AI Sentinel backend activ!",
        "status": "online"
    }), 200

# ✅ Preluare active din baza de date
@app.route("/api/portfolio", methods=["GET"])
def get_portfolio():
    assets = Portfolio.query.all()
    data = [a.to_dict() for a in assets]
    return jsonify(data), 200

# ✅ Adăugare activ nou
@app.route("/api/add", methods=["POST"])
def add_asset():
    try:
        data = request.get_json()
        symbol = data.get("symbol")
        value = float(data.get("value"))
        new_item = Portfolio(symbol=symbol, value=value)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"status": "added", "asset": new_item.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# ✅ Optimizare portofoliu cu AI
@app.route("/api/optimize", methods=["POST"])
def optimize():
    data = request.get_json()
    suggestion = recommend_portfolio(data.get("assets", []))
    return jsonify(suggestion), 200

# ✅ Resetare completă a bazei
@app.route("/api/reset", methods=["DELETE"])
def reset():
    Portfolio.query.delete()
    db.session.commit()
    return jsonify({"status": "reset complete"}), 200

# ✅ Punct de pornire principal (Render și local)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
