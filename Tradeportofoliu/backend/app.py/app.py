from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db, Portfolio
from ai_optimizer import recommend_portfolio

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tradeportofoliu.db"
db.init_app(app)

@app.route("/api/portfolio", methods=["GET"])
def get_portfolio():
    assets = Portfolio.query.all()
    return jsonify([a.to_dict() for a in assets])

@app.route("/api/add", methods=["POST"])
def add_asset():
    data = request.get_json()
    new_item = Portfolio(symbol=data["symbol"], value=data["value"])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"status": "added", "asset": new_item.to_dict()})

@app.route("/api/optimize", methods=["POST"])
def optimize():
    data = request.get_json()
    suggestion = recommend_portfolio(data["assets"])
    return jsonify(suggestion)

@app.route("/api/reset", methods=["DELETE"])
def reset():
    Portfolio.query.delete()
    db.session.commit()
    return jsonify({"status": "reset complete"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
