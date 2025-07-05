from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("homepage.html")

@app.route("/catalogue", methods=["GET", "POST"])
def catalogue():
    return render_template("catalog.html")

if __name__ == '__main__':
    app.run(debug=True)
