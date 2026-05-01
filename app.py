from flask import Flask, request, render_template
from utils.evaluator import evaluate_answers

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Server is Running successful"


# Submit Test Route
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


# Run Server
if __name__ == '__main__':
    app.run(debug=True)