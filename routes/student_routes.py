from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route('/')
def dashboard():
    return render_template('student/dashboard.html')

@student.route('/profile')
def profile():
    return render_template('student/profile.html')

@student.route('/edit-profile')
def edit_profile():
    return render_template('student/edit_profile.html')

@student.route('/applications')
def applications():
    return render_template('student/applications.html')

@student.route('/test')
def test():
    return render_template('student/test.html')