import mysql.connector
import os
from dotenv import load_dotenv

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, ".env")

# Force load_dotenv to look in the script's directory
load_dotenv(dotenv_path=env_path)

mysql_host = os.getenv("MYSQL_URL")
mysql_username = os.getenv("MYSQL_USERNAME")
mysql_password = os.getenv("MYSQL_PASSWORD")

# Debugging check (will fail safely if variables are missing)
if not mysql_password:
    print(f"DEBUG ERROR: MYSQL_PASSWORD was not found! Loaded from: {env_path}")

def store_transaction_result(transaction, status, duration, timestamp):
    try:
        conn = mysql.connector.connect(
            host=mysql_host,
            user=mysql_username,
            password=mysql_password,
            database="appium"
        )
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO appium_android_calculator (RunTimeStamp, Transaction, Status, Duration)
            VALUES (%s, %s, %s, %s)
        """, (timestamp, transaction, status, duration))

        conn.commit()
        cursor.close()
        conn.close()

        print(f"MySQL: Stored result for {transaction} ({status})")

    except Exception as e:
        print(f"MySQL logging failed: {e}")
