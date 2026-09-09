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
run_type = ""

if "JENKINS_SERVER_COOKIE" in os.environ or "BUILD_NUMBER" in os.environ:
    print("\nWe are running from Jenkins")
    run_type = "jenkins"
else:
    print("\nWe are NOT running from Jenkins - need to set MySQL URL accordingly")
    run_type = "manual"

def store_transaction_result(test_name, transaction, status, duration, timestamp):
    try:
        conn = mysql.connector.connect(
            host=mysql_host,
            user=mysql_username,
            password=mysql_password,
            database="appium",
        )
        cursor = conn.cursor()

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