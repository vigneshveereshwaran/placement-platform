from flask import Flask, render_template

app = Flask(__name__)

# =========================================
# AUTH PAGES
# =========================================

@app.route('/')
def login():
    return render_template(
        'auth/login.html'
    )


@app.route('/register')
def register():
    return render_template(
        'auth/register.html'
    )


@app.route('/forgot-password')
def forgot_password():
    return render_template(
        'auth/forgot_password.html'
    )


# =========================================
# ADMIN PAGES
# =========================================

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template(
        'admin/admin_dashboard.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


@app.route('/manage-students')
def manage_students():
    return render_template(
        'admin/manage_students.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


@app.route('/add-student')
def add_student():
    return render_template(
        'admin/add_student.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


@app.route('/manage-companies')
def manage_companies():
    return render_template(
        'admin/manage_companies.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


@app.route('/add-company')
def add_company():
    return render_template(
        'admin/add_company.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


# =========================================
# STUDENT PAGES
# =========================================

@app.route('/student-dashboard')
def student_dashboard():
    return render_template(
        'student/student_dashboard.html',

        student_navbar=True,

        show_dashboard=True,
        show_companies=True,
        show_applications=True,
        show_profile=True
    )


@app.route('/companies')
def companies():
    return render_template(
        'student/companies.html',

        student_navbar=True,

        show_dashboard=True,
        show_companies=True,
        show_applications=True,
        show_profile=True
    )


@app.route('/applications')
def applications():
    return render_template(
        'student/applications.html',

        student_navbar=True,

        show_dashboard=True,
        show_companies=True,
        show_applications=True,
        show_profile=True
    )


@app.route('/profile')
def profile():
    return render_template(
        'student/profile.html',

        student_navbar=True,

        show_dashboard=True,
        show_companies=True,
        show_applications=True,
        show_profile=True
    )


# =========================================
# COMPANY PAGES
# =========================================

@app.route('/company-dashboard')
def company_dashboard():
    return render_template(
        'company/company_dashboard.html',

        company_navbar=True,

        show_dashboard=True,
        show_post_job=True,
        show_applications=True
    )


@app.route('/post-job')
def post_job():
    return render_template(
        'company/post_job.html',

        company_navbar=True,

        show_dashboard=True,
        show_post_job=True,
        show_applications=True
    )


@app.route('/selected-students')
def selected_students():
    return render_template(
        'company/selected_students.html',

        company_navbar=True,

        show_dashboard=True,
        show_post_job=True,
        show_applications=True
    )


# =========================================
# NOTIFICATIONS PAGE
# =========================================

@app.route('/notifications')
def notifications():
    return render_template(
        'notifications/notifications.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


# =========================================
# REPORTS PAGE
# =========================================

@app.route('/reports')
def reports():
    return render_template(
        'admin/reports.html',

        admin_navbar=True,

        show_dashboard=True,
        show_students=True,
        show_add_student=True,
        show_companies=True,
        show_add_company=True,
        show_notifications=True
    )


# =========================================
# LOGOUT
# =========================================

@app.route('/logout')
def logout():
    return render_template(
        'auth/login.html'
    )


# =========================================
# RUN APP
# =========================================

if __name__ == '__main__':
    app.run(debug=True)