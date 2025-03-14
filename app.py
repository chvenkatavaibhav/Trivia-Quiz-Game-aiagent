from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

# Store fetched questions in memory
stored_questions = []

def fetch_questions(category_id, difficulty, num_questions=10):
    url = "https://opentdb.com/api.php"
    params = {
        "amount": num_questions,
        "category": category_id,
        "difficulty": difficulty,
        "type": "multiple",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start_quiz", methods=["POST"])
def start_quiz():
    global stored_questions
    data = request.json
    category_id = int(data["category"])
    difficulty = data["difficulty"]
    num_questions = int(data["num_questions"])

    # Fetch new questions only if stored_questions is empty
    if not stored_questions:
        questions = fetch_questions(category_id, difficulty, num_questions)
        if questions:
            stored_questions = questions  # Store questions for reuse
            random.shuffle(stored_questions)  # Shuffle questions
        else:
            return jsonify({"error": "Failed to fetch questions"}), 500

    return jsonify(stored_questions)

@app.route("/reset_quiz", methods=["POST"])
def reset_quiz():
    global stored_questions
    stored_questions = []  # Clear stored questions
    return jsonify({"status": "Quiz reset"})

if __name__ == "__main__":
    app.run(debug=True)