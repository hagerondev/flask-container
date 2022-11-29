from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello UEC!"

if __name__ == "__main__":
    serve(app, port=80)