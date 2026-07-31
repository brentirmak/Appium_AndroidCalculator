import mysql.connector
import os
from dotenv import load_dotenv

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Retrieve the secrets using os.getenv()
mysql_host = os.getenv("MYSQL_URL")
mysql_username = os.getenv("MYSQL_USERNAME")
mysql_password = os.getenv("MYSQL_PASSWORD")

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
