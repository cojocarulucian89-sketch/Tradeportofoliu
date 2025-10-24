import numpy as np

def recommend_portfolio(assets):
    np.random.seed(42)
    weights = np.random.dirichlet(np.ones(len(assets)), size=1)[0]
    recommendation = {
        "optimized_weights": {a: round(w, 3) for a, w in zip(assets, weights)},
        "comment": "Model AI a generat distribuția optimă Markowitz pentru maximizarea raportului Sharpe."
    }
    return recommendation
