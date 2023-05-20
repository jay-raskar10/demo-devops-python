from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This html file,is rendered in flask and hosted on server,& is accessible globally</h1>"

if __name__ == "__main__":
    app.run()
