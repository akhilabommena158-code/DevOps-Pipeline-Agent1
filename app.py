from flask import Flask, render_template, request, jsonify
from agent import analyze_project

app = Flask(__name__)


# -----------------------------
# Home page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Health check
# -----------------------------
@app.route("/api/health")
def health():
    return jsonify({
        "status": "online",
        "message": "Hindsight AI DevOps Agent is running"
    })


# -----------------------------
# Project analysis API
# -----------------------------
@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "No data received."
        }), 400

    url = data.get("url", "").strip()
    mode = data.get("mode", "repository")

    if not url:
        return jsonify({
            "success": False,
            "error": "Please enter a project URL."
        }), 400

    try:

        result = analyze_project(
            url,
            mode
        )

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 500


# -----------------------------
# Start Flask server
# -----------------------------
if __name__ == "__main__":

    print("=" * 50)
    print("HINDSIGHT AI DEVOPS AGENT")
    print("=" * 50)
    print("Server starting...")
    print("Open: http://127.0.0.1:5000")
    print("=" * 50)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )