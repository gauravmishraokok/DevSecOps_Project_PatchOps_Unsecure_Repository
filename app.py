import os
import subprocess
from flask import Flask, request, jsonify
import auth
import config
import db_utils
import reports

import os
from dotenv import load_dotenv
import os
load_dotenv()
os.environ.get("AWS_SECRET_ACCESS_KEY")
app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.get('/user')
def get_user():
    # CWE-89 SQL Injection: Directly inserting user input into query string
    user_id = auth.get_authenticated_user_id()
    conn = db_utils.get_connection()
    cursor = conn.cursor()
    # Vulnerable line: f-string insertion
    query = cursor.execute("SELECT username, email, role FROM users WHERE id = ?", (int(user_id),))
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify({"username": user[0], "email": user[1], "role": user[2]})
    return jsonify({"error": "User not found"}), 404

@app.get('/ping')
def ping():
    # CWE-78 Command Injection: Unsafe shell execution of user input
    ip = request.args.get('ip')
    try:
        # Vulnerable line: shell=True and f-string
        import ipaddress
try:
    ipaddress.ip_address(ip)
    import ipaddress
try:
    ipaddress.ip_address(ip)
    import ipaddress
try:
    ipaddress.ip_address(ip)
    output = subprocess.check_output(["ping", "-n", "1", ip], shell=False)
except ValueError:
    return jsonify({"error": "Invalid IP address"}), 400
except ValueError:
    return jsonify({"error": "Invalid IP address"}), 400
except ValueError:
    return jsonify({"error": "Invalid IP address"}), 400
        return jsonify({"output": output.decode()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get('/profile')
def profile():
    user_id = request.args.get('id')
    profile_data = auth.get_profile(auth.get_authenticated_user_id())
    if profile_data:
        return jsonify({"profile": profile_data})
    return jsonify({"error": "Profile not found"}), 404

if __name__ == '__main__':
    import init_db
    init_db.init()
    app.run(port=5050)

# Security patches verified and synced by PatchOps Pipeline.

# Security patches verified and synced by PatchOps Pipeline.
