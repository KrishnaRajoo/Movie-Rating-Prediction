from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("movie_rating_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ==========================
        # Get Form Data
        # ==========================

        year = request.form.get("year")
        duration = request.form.get("duration")
        votes = request.form.get("votes")

        genre = request.form.get("genre")
        director = request.form.get("director")
        actor1 = request.form.get("actor1")
        actor2 = request.form.get("actor2")
        actor3 = request.form.get("actor3")

        # ==========================
        # Validation
        # ==========================

        if not all([
            year,
            duration,
            votes,
            genre,
            director,
            actor1,
            actor2,
            actor3
        ]):

            return render_template(
                "index.html",
                error="⚠ Please fill all the fields."
            )

        year = float(year)
        duration = float(duration)
        votes = float(votes)

        # If you used log1p during training,
        # keep this line.
        votes = np.log1p(votes)

        # ==========================
        # Create Input DataFrame
        # ==========================

        input_data = pd.DataFrame({

            "Year": [year],
            "Duration": [duration],
            "Votes": [votes],
            "Genre": [genre],
            "Director": [director],
            "Actor 1": [actor1],
            "Actor 2": [actor2],
            "Actor 3": [actor3]

        })

        # ==========================
        # Prediction
        # ==========================

        prediction = model.predict(input_data)[0]

        prediction = round(float(prediction), 2)

        # ==========================
        # Movie Quality
        # ==========================

        if prediction >= 8:

            quality = "🌟 Excellent Movie"

            color = "#22c55e"

        elif prediction >= 6:

            quality = "🎬 Good Movie"

            color = "#3b82f6"

        elif prediction >= 4:

            quality = "👍 Average Movie"

            color = "#f59e0b"

        else:

            quality = "👎 Below Average"

            color = "#ef4444"

        return render_template(

            "index.html",

            prediction=prediction,

            quality=quality,

            color=color

        )

    except Exception as e:

        return render_template(

            "index.html",

            error=f"Prediction Error: {str(e)}"

        )


if __name__ == "__main__":

    app.run(debug=True)