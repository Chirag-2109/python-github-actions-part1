from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Deployed with GitHub Actions — Hello class!</h1>"

if __name__ == "__main__":
    # for local dev only; Heroku will use gunicorn
    app.run(host="0.0.0.0", port=8000)
