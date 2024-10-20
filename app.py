from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="iit_indore_db"
)
cursor = db.cursor()

# Home page with login and registration forms
@app.route('/')
def index():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['user_id']
    mobile_number = request.form['mobile_number']
    password = request.form['password']

    cursor.execute("INSERT INTO users (user_id, mobile_number, password) VALUES (%s, %s, %s)", (user_id, mobile_number, password))
    db.commit()
    flash("Registration successful! Please login.")
    return redirect(url_for('index'))

# Login route
@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    password = request.form['password']

    cursor.execute("SELECT * FROM users WHERE user_id=%s AND password=%s", (user_id, password))
    user = cursor.fetchone()

    if user:
        # Fetch all available courses for BTech, CSE@IITI
        cursor.execute("SELECT course_code, course_name, credits, semester FROM courses")
        courses = cursor.fetchall()  # Fetch all course details
        return render_template('welcome.html', courses=courses)
    else:
        flash("Invalid UserID or Password!")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
