🎓 Student Performance Prediction System

📌 Project Overview

The Student Performance Prediction System is a rule-based web application that evaluates a student’s academic performance using key indicators such as past average marks, attendance percentage, and daily study hours.
Instead of machine learning or datasets, the system uses a weighted mathematical formula, making the results transparent, explainable, and easy to validate.

🎯 Objectives
	•	To predict student performance without using datasets or ML models
	•	To provide an interpretable and simple evaluation mechanism
	•	To ensure final performance scores do not exceed 100
	•	To build a beginner-friendly academic project using Flask

🛠️ Technologies Used
	•	Frontend: HTML, CSS
	•	Backend: Python (Flask)
	•	Logic: Rule-based weighted formula
	•	Environment: Python 3.x

🧮 Performance Calculation Formula

Performance Score =
(W1 × Past Average Marks) +
(W2 × Attendance Percentage) +
(W3 × Normalized Study Hours)

Weight Values:
	•	W1 (Past Average) = 0.5
	•	W2 (Attendance) = 0.3
	•	W3 (Study Hours) = 0.2

Normalization:

Normalized Study Hours = (Study Hours / 10) × 100

Final Score:

Final Marks = min(Performance Score, 100)

📂 Project Structure

Student_performance_prediction/
│── app.py
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

🚀 How to Run the Project

1️⃣ Install Required Packages

python3 -m pip install flask

2️⃣ Run the Application

python3 app.py

3️⃣ Open in Browser

http://127.0.0.1:5000


👤 User Inputs
	•	Past Average Marks (0–100)
	•	Attendance Percentage (0–100)
	•	Study Hours per Day

📤 Output
	•	Displays the final performance score
	•	Ensures the score never exceeds 100
	•	Provides error messages for invalid inputs

🎓 Key Features
	•	No dataset required
	•	No machine learning dependency
	•	Transparent and explainable logic
	•	Clean and responsive user interface
	•	Suitable for college projects, demos, and viva

📖 Viva Explanation (Short)

This project uses a rule-based weighted formula to evaluate student performance.
It avoids machine learning to ensure transparency and ease of interpretation, while a capping mechanism ensures academic score limits are maintained.

🔮 Future Enhancements
	•	Grade classification (A, B, C, Fail)
	•	Performance feedback & suggestions
	•	Progress bar visualization
	•	PDF report generation
	•	React-based frontend
