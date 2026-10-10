from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Initialize database table
def init_db():
    conn = sqlite3.connect("netflix.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email", "").strip().lower()
    if "@" not in email:
        return jsonify({"message": "Please enter a valid email"}), 400

    conn = sqlite3.connect("netflix.db")
    try:
        conn.execute("INSERT INTO users (email) VALUES (?)", (email,))
        conn.commit()
        message = "Account created!"
    except sqlite3.IntegrityError:
        message = "This email is already registered"
    finally:
        conn.close()
    return jsonify({"message": message})

@app.route("/users")
def users():
    conn = sqlite3.connect("netflix.db")
    rows = conn.execute("SELECT id, email, created_at FROM users").fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)