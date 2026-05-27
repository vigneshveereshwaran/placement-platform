from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add-student')
def add_student():
    return render_template('admin/add_student.html')


@app.route('/add-company')
def add_company():
    return render_template('admin/add_company.html')


@app.route('/manage-companies')
def manage_companies():
    return render_template('admin/manage_companies.html')


@app.route('/notifications')
def notifications():
    return render_template('notifications/notifications.html')


if __name__ == '__main__':
@app.route("/")
def home():
    return render_template("admin/dashboard.html")

@app.route("/add-student")
def add_student():
    return render_template("admin/add_student.html")

@app.route("/manage-students")
def manage_students():
    return render_template("admin/manage_students.html")

if __name__ == "__main__":
    app.run(debug=True)