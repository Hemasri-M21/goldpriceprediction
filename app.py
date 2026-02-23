from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("gold_model.pkl", "rb"))

@app.route("/", methods=["GET","POST"])
def home():
    prediction = None

    if request.method == "POST":
        spx = float(request.form["spx"])
        oil = float(request.form["oil"])
        slv = float(request.form["slv"])
        eurusd = float(request.form["eurusd"])

        data = np.array([[spx, oil, slv, eurusd]])
        prediction = model.predict(data)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)