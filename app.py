from flask import Flask, request, render_template
from utils.evaluator import evaluate_answers
from utils.db import check_user, add_user,get_all_users,delete_user
from flask import redirect, url_for

app = Flask(__name__)


# 🔹 Home → Login Page
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/delete_user/<int:user_id>')
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('login'))
    

# 🔹 Login Logic
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = check_user(username, password)

    print(user)  # debug (you can remove later)

    if user:
        role = user[3]   # ✅ correct index

        if role == "admin":
            if role == "admin":
                users = get_all_users()
                return render_template("admin.html", users=users)
        else:
            return render_template("test.html")

    return render_template("login.html", error="Invalid Login")


# 🔹 Admin adds user
@app.route('/add_user', methods=['POST'])
def add_user_route():
    username = request.form['username']
    password = request.form['password']

    add_user(username, password)

    return "User Added Successfully"


# 🔹 Existing pages (KEEP SAME)
@app.route('/statistics')
def statistics():
    return render_template('statistics.html')


@app.route('/notifications')
def notifications():
    return render_template('notifications.html')


@app.route('/test')
def test():
    return render_template('test.html')


# 🔹 Submit Test
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


# 🔹 Run server
if __name__ == '__main__':
    app.run(debug=True)