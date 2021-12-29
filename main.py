from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested


@app.route("/")
def index():
    return "Hallo wereld!"


@app.route("/final")
def final():
    return "My final assignment!!!"


@app.route("/cow")
def cow():
    return "MOoooOo!"


if __name__ == "__main__":
    app.run()
