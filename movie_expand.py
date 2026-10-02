from flask import Flask, request, redirect, url_for, render_template_string, session
from db import get_db, init_db
import bcrypt
import re

movie = Flask(__name__)

users = {
    "elliot": "123abc"
}
base_style = """
<style>
body {
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.card {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    width: 300px;
    text-align: center;
}
input {
    width: 90%;
    padding: 8px;
    margin: 8px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}
button {
    padding: 10px;
    width: 60%;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background: #45a049;
}
a {
    display: block;
    margin-top: 10px;
    color: #333;
    text-decoration: none;
}
.error {
    color: red;
    margin-top: 10px;
}
</style>
"""

login_page = base_style + """
<div class="card">
<h2>Login</h2>
<form method="POST">
  <input name="username" placeholder="Username"><br>
  <input name="password" type="password" placeholder="Password"><br>
  <button type="submit">Login</button>
</form>
<a href="/register">Create an account</a>
<p class="error">{{ error }}</p>
</div>
"""

register_page = base_style + """
<div class="card">
<h2>Register</h2>
<form method="POST">
  <input name="username" placeholder="Username"><br>
  <input name="password" type="password" placeholder="Password"><br>
  <button type="submit">Sign Up</button>
</form>
<a href="/">Back to login</a>
<p class="error">{{ error }}</p>
</div>
"""

secret_page = base_style + """
<div class="card">
<h2>🎉 Secret Room</h2>
<h3>Welcome, {{ username }}!</h3>
<p>You got into the secret room!</p>
<a href="/logout"><button>Logout</button></a>
</div>
"""
def is_valid_password(password):
    return (
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[^A-Za-z0-9]", password)
    )

# ---------- ROUTES ----------
@movie.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Incorrect username or password"

    return render_template("login.html", error=error)

@movie.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            error = "Fields cannot be empty"
        elif not is_valid_password(password):
            error = "Password must include uppercase, lowercase, number, and special character"
        else:
            conn = get_db()
            try:
                hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

                conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hashed_pw)
                )
                conn.commit()

                return redirect(url_for("login"))
            except:
                conn.rollback()
                error = "Username already exists or error occurred"
            finally:
                conn.close()

    return render_template("register.html", error=error)

@movie.route("/dashboard")
def dashboard():
    # TODO: RENAME THIS ROUTE TO /dashboard
    # TODO: Connect to the database
    # TODO: Get all entries that belong to the logged-in user
    # TODO: Close the connection
    # TODO: Pass entries into your template
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    entries = conn.execute(
        "SELECT * FROM entries WHERE user=?",
        (session["user"],)
    ).fetchall()
    conn.close()
    #return render_template_string(page, entries=entries)
    #return render_template("dashboard.html", entries=entries, username=session["user"])


    # TEMPORARY (remove later)
    return render_template("dashboard.html", entries=entries, username=session["user"])

@movie.route("/create", methods=["GET", "POST"])
def create():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["Title"]
        content = request.form["Content"]
        image = request.form["Image"]

        conn = get_db()
        conn.execute(
            "INSERT INTO entries (title, content, image, user) VALUES (?, ?, ?, ?)",
            (title, content, image, session["user"])
        )

        conn.commit()
        conn.close()
        return redirect(url_for("dashboard"))
    return render_template("create.html", username=session["user"])


# ---------- UPDATE ----------
# TODO: Create a route like /edit/<id>
# This page should:
# - Load existing data
# - Show it in a form
# - Update the database on submit


@movie.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()

    entry = conn.execute(
        "SELECT * FROM entries WHERE id=? AND user=?",
        (id, session["user"])
    ).fetchone()

    if not entry:
        conn.close()
        return "Not allowed"

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        image = request.form["image"]

        conn.execute(
            "UPDATE entries SET title=?, content=?, image=? WHERE id=?",
            (title, content, image, id)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("dashboard"))

    return render_template("edit.html", entry=entry)

# ---------- DELETE ----------
# TODO: Create a route like /delete/<id>
# This should:
# - Delete an entry from the database
# - Redirect back to dashboard
    # TODO: Connect to database
    # TODO: Delete entry WHERE id AND user
    # TODO: Commit and close
@movie.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    entry = conn.execute(
        "SELECT * FROM entries WHERE id=? AND user=?",
        (id, session["user"])
    ).fetchone()

    if not entry:
        conn.close()
        return "Entry not found"

    if request.method == "POST":
        try:
            conn.execute(
                "DELETE FROM entries WHERE id=? AND user=?",
                (id, session["user"])
                )
            conn.commit()
        finally:
            conn.close()
        return redirect(url_for("dashboard"))

    conn.close()
    return render_template("delete.html", entry=entry)



@movie.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------- RUN ----------
if __name__ == "__main__":
    movie.run(debug=True)