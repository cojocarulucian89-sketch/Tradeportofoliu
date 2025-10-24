from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '✅ NEWTRADE Pro – Server activ! AI Sentinel pregătit.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
