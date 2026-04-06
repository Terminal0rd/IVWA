from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

modules = {
    "sqli": {
        "title": "SQL Injection Lab",
        "description": "Login system is vulnerable...",
        "goal": "Bypass login using SQL Injection"
    },
    "auth": {
        "title": "Broken Authentication",
        "description": "Session tokens are predictable...",
        "goal": "Hijack user session"
    },
    "xss": {
        "title": "Cross-Site Scripting",
        "description": "User input is reflected...",
        "goal": "Execute JavaScript in browser"
    }
}

@app.route("/module/<name>", methods=["GET", "POST"])
def module(name):
    module_data = modules.get(name)

    if not module_data:
        return "Module not found", 404

    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # (keep your SQLi logic for now)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(f"/lab/{name}")
        else:
            message = "Invalid Credentials ❌"

    return render_template(
        "module.html",
        module=module_data,
        message=message
    )

from flask import redirect

@app.route("/lab/<name>")
def lab(name):
    return f"This is {name} vulnerability lab"

@app.route("/lab/xss", methods=["GET", "POST"])
def xss_lab():
    comment = ""

    if request.method == "POST":
        comment = request.form.get("comment")

    return render_template("xss_lab.html", comment=comment)

if __name__ == "__main__":
    app.run(debug=True)