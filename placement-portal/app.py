@app.route('/add-student')
def add_student():
    return render_template('add_student.html')

@app.route('/add-company')
def add_company():
    return render_template('add_company.html')

@app.route('/manage-companies')
def manage_companies():
    return render_template('manage_companies.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')