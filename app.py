from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

CORS(app)

model = joblib.load(
    os.path.join(BASE_DIR, "..", "model", "airbnb_model.pkl")
)






# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN PAGE ----------------

@app.route("/login")
def login():
    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- PREDICTION ----------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.json

        input_data = pd.DataFrame({
            "neighbourhood group":[data["location"]],
            "room type":[data["room_type"]],
            "minimum nights":[int(data["minimum_nights"])],
            "number of reviews":[int(data["reviews"])],
            "availability 365":[int(data["availability"])]
        })

        prediction = model.predict(input_data)

        return jsonify({
            "predicted_price": round(prediction[0],2)
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)