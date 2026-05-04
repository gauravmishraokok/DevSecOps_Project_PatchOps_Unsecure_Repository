from flask import Flask, request, jsonify
import db_utils
import auth
import config
import reports
import subprocess
import os

app = Flask(__name__)

@app.route('/user')
def get_user():
    # CWE-89 SQL Injection
    user_id = request.args.get('id')
    if not user_id:
        return jsonify({"error": "missing id"}), 400
    conn = db_utils.get_connection()
    cursor = conn.cursor()
    query = "SELECT username, email, role FROM users WHERE id = %s"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    if users:
        return jsonify({"users": users})
    return jsonify({"error": "not found"}), 404

@app.route('/ping')
def ping():
    # CWE-78 Command Injection
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "missing ip"}), 400
    try:
        # Vulnerable command execution
        output = subprocess.check_output(["ping", "-n", "1", ip], stdout=subprocess.PIPE) 
        return f"<pre>{output.decode()}</pre>"
    except Exception as e:
        return str(e), 500

@app.route('/profile/<id>')
def profile(id):
    p = auth.get_profile(id)
    if p:
        return jsonify({"profile": p})
    return jsonify({"error": "not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)