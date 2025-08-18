from flask import Flask, abort, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path
import os

app = Flask(__name__)

db = 'database/users.db'

@app.route("/")
def home():
    return "<h1>Hello, World</h1>"

@app.route("/about/")
def about():
    return "<h1>About Page</h1>"

@app.route("/submit/", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        # Form validation
        username = request.form.get('username')
        email = request.form.get('email')
        name = request.form.get('name')
        age = request.form.get('age')

        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        try:
            cursor.execute("insert into users (username, email, name, age) values (?, ?, ?, ?)", (username, email, name, age))
            conn.commit()
            return redirect(url_for("user",username=username))
        except sqlite3.Error as e:
            return f"Database error: {e}", 500
        finally:
            conn.close()

    return render_template("form.html")

@app.route("/user/<username>/")
def user(username):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('select * from users where username= ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        abort(404, description='User not found')

    user_data = {
        'username': user[1],
        'email': user[2],
        'name': user[3],
        'age': user[4]
    }

    return render_template('index.html', user=user_data)

if __name__ == "__main__":
    app.run(debug=True)
