from flask import Flask, render_template, request, jsonify
from backend.engine import run_user_code, check_output, award_tracker, get_next_challenge
from backend.challenges import challenges

app = Flask(__name__)
index = 0
score = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_challenge", methods=["GET"])
def get_challenge():
    global index
    challenge = get_next_challenge(index, challenges)
    if challenge:
        return jsonify({"code": challenge["code"], "index": index})
    return jsonify({"message": "completed"})

@app.route("/submit_code", methods=["POST"])
def submit_code():
    global score, index
    data = request.get_json()
    user_code = data.get("code")
    challenge = get_next_challenge(index, challenges)
    expected = challenge["expected_output"]
    output = run_user_code(user_code)
    is_correct = check_output(output, expected)

    if is_correct:
        score += 1

    response = {
        "correct": is_correct,
        "your_output": output,
        "expected": expected,
        "score": score,
        "stars": "⭐" * award_tracker(score)
    }

    index += 1
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from backend.engine import run_user_code, check_output, award_tracker, get_next_challenge
from backend.challenges import challenges

app = Flask(__name__)
index = 0
score = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_challenge", methods=["GET"])
def get_challenge():
    global index
    challenge = get_next_challenge(index, challenges)
    if challenge:
        return jsonify({"code": challenge["code"], "index": index})
    return jsonify({"message": "completed"})

@app.route("/submit_code", methods=["POST"])
def submit_code():
    global score, index
    data = request.get_json()
    user_code = data.get("code")
    challenge = get_next_challenge(index, challenges)
    expected = challenge["expected_output"]
    output = run_user_code(user_code)
    is_correct = check_output(output, expected)

    if is_correct:
        score += 1

    response = {
        "correct": is_correct,
        "your_output": output,
        "expected": expected,
        "score": score,
        "stars": "⭐" * award_tracker(score)
    }

    index += 1
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
