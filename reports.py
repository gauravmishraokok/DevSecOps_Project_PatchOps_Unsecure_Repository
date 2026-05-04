import db_utils
import config

def generate_user_report(user_id):
    # Safe report generation
    results = db_utils.safe_query("SELECT * FROM reports WHERE user_id = ?", (user_id,))
    return results

def export_csv():
    return "id,title,content\n1,Report 1,Content 1"
