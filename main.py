from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/module/<name>", methods=["GET", "POST"])
def module(name):
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Connect to DB
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # SAFE query (parameterized)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()

        conn.close()

        if user:
            message = "Login Successful ✅"
        else:
            message = "Invalid Credentials ❌"

    return render_template("module.html", module_name=name, message=message)

if __name__ == "__main__":
    app.run(debug=True)