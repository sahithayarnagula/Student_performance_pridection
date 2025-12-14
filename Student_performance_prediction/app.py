from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Take user inputs
            past_avg = float(request.form["past_avg"])
            attendance = float(request.form["attendance"])
            study_hours = float(request.form["study_hours"])

            # Input validation
            if not (0 <= past_avg <= 100):
                raise ValueError("Past average must be between 0 and 100")

            if not (0 <= attendance <= 100):
                raise ValueError("Attendance must be between 0 and 100")

            if study_hours < 0:
                raise ValueError("Study hours cannot be negative")

            # Weights
            W1 = 0.5   # Past Average
            W2 = 0.3   # Attendance
            W3 = 0.2   # Study Hours

            # Normalize study hours (max 10 hrs/day)
            normalized_study_hours = min((study_hours / 10) * 100, 100)

            # Performance score calculation
            score = (
                (W1 * past_avg) +
                (W2 * attendance) +
                (W3 * normalized_study_hours)
            )

            # Ensure final marks do not exceed 100
            prediction = min(round(score, 2), 100)

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)