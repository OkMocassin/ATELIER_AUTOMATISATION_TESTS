from flask import Flask, render_template, jsonify
from tester.runner import run_tests
from storage import init_db, save_run, list_runs

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return "API Monitoring actif"

@app.route("/run")
def run():
    data = run_tests()
    save_run(data)
    return jsonify(data)

@app.route("/health")
def health():
    return {
        "status": "OK",
        "service": "API Monitoring",
        "uptime": "running"
    }

@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    return render_template("dashboard.html", runs=runs)
