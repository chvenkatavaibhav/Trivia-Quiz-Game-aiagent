from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Open Trivia Database API URL
API_URL = "https://opentdb.com/api.php"

# Categories and their corresponding IDs
CATEGORIES = {
    "General Knowledge": 9,
    "Science & Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Animals": 27,
}

# Difficulty levels
DIFFICULTY_LEVELS = ["easy", "medium", "hard"]


def fetch_questions(category_id, difficulty, num_questions=10):
    """Fetch questions from the Open Trivia Database API."""
    params = {
        "amount": num_questions,
        "category": category_id,
        "difficulty": difficulty,
        "type": "multiple",  # Multiple-choice questions
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return None


@app.route("/")
def home():
    """Render the home page with category and difficulty options."""
    return render_template("index.html", categories=CATEGORIES, difficulties=DIFFICULTY_LEVELS)


@app.route("/start_quiz", methods=["POST"])
def start_quiz():
    """Start the quiz by fetching questions based on user selections."""
    data = request.json
    category_id = CATEGORIES[data["category"]]
    difficulty = data["difficulty"]
    questions = fetch_questions(category_id, difficulty)
    if questions:
        return jsonify(questions)
    else:
        return jsonify({"error": "Failed to fetch questions"}), 500


@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    """Check if the user's answer is correct."""
    data = request.json
    user_answer = data["user_answer"]
    correct_answer = data["correct_answer"]
    return jsonify({"correct": user_answer == correct_answer})


if __name__ == "__main__":
    app.run(debug=True)
