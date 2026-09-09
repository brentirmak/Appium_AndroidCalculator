import os
import mysql.connector
from dotenv import load_dotenv

# ============================================================
# Load environment variables
# ============================================================

load_dotenv()

mysql_host = os.getenv("MYSQL_URL")
mysql_username = os.getenv("MYSQL_USERNAME")
mysql_password = os.getenv("MYSQL_PASSWORD")

def get_run_type():
    if "JENKINS_SERVER_COOKIE" in os.environ or "BUILD_NUMBER" in os.environ:
        return "jenkins"
    return "manual"

def store_transaction_result(test_name, transaction, status, duration, timestamp):
    try:
        conn = mysql.connector.connect(
            host=mysql_host,
            user=mysql_username,
            password=mysql_password,
            database="appium",
        )
        cursor = conn.cursor()

        run_type = get_run_type()

        cursor.execute(
            """
            INSERT INTO appium_android_calculator (RunTimeStamp, RunType, TestName, Transaction, Status, Duration)
            VALUES (%s, %s, %s, %s, %s, %s)
        """,
            (timestamp, run_type, test_name, transaction, status, duration),
        )

        conn.commit()
        cursor.close()
        conn.close()

        print(
            f"MySQL: Stored result for {test_name} - {transaction} ({status})"
        )

    except Exception as e:
        print(f"MySQL logging failed: {e}")