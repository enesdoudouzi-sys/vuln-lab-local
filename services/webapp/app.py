from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Local Security Lab"

@app.route("/search")
def search():
    term = request.args.get("q", "")

    # absichtlich keine Prepared Statements → SQL Injection Demo (nur lokal!)
    conn = mysql.connector.connect(
        host="db",
        user="test",
        password="test123",
        database="testdb"
    )
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name LIKE '%{term}%';"
    cursor.execute(query)
    results = cursor.fetchall()

    return {"query": query, "results": results}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
