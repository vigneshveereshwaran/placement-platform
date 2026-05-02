from flask import Flask, render_template

app = Flask(__name__)

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

if __name__ == '__main__':
    app.run(debug=True)