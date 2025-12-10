from flask import Flask, request

app = Flask(__name__)

SECRET = "1234"  # absichtlich schwach

@app.route("/admin")
def admin():
    token = request.args.get("token")
    if token == SECRET:
        return "Admin access granted"
    return "Access denied"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
