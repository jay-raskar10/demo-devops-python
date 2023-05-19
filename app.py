from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This html file is rendered in flask application which is hosted on server.</h1>"

if __name__ == "__main__":
    app.run()
