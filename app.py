from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("gold_model.pkl", "rb"))

@app.route("/", methods=["GET","POST"])
def home():
    prediction = None
    spx = oil = slv = eurusd = ""

    if request.method == "POST":
        spx = request.form["spx"]
        oil = request.form["oil"]
        slv = request.form["slv"]
        eurusd = request.form["eurusd"]

        data = np.array([[float(spx), float(oil), float(slv), float(eurusd)]])
        prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        spx=spx,
        oil=oil,
        slv=slv,
        eurusd=eurusd
    )

if __name__ == "__main__":
    app.run(debug=True)