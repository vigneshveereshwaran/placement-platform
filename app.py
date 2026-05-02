from flask import Flask, request, render_template
from utils.evaluator import evaluate_answers

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Running successful"

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/submit_test', methods=['POST'])
def submit_test():
    user_answers = request.form.to_dict()
    result = evaluate_answers(user_answers)

    return render_template(
        "result.html",
        score=result["score"],
        total=result["total"],
        percentage=result["percentage"]
    )