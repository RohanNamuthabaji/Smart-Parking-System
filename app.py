from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="smart_parking"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        return redirect('/dashboard')
    else:
        return "Login Failed"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['root123']

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()

    return redirect('/')

@app.route('/dashboard')
def dashboard():
    cursor.execute("SELECT slot FROM bookings")
    booked = cursor.fetchall()

    booked_slots = [b[0] for b in booked]

    return render_template("dashboard.html", booked_slots=booked_slots)

@app.route('/book', methods=['POST'])
def book():
    slot = request.form['slot']
    username = "user1"

    # simple payment simulation
    fee = 50
    print(f"Payment of ₹{fee} successful for slot {slot}")

    cursor.execute("INSERT INTO bookings (username, slot) VALUES (%s, %s)", (username, slot))
    db.commit()

    return redirect('/dashboard')

app.run(debug=True)