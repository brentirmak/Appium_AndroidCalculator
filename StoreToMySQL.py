import mysql.connector
from datetime import datetime
import pytz

def store_to_mysql(trx_dict):
    print("We are inside the store_to_mysql function")

    if "Home" in trx_dict:
        home_transaction = round(trx_dict['Home'],4)
    else:
        home_transaction = 'NULL'
    if "Access Basic Calculator" in trx_dict:
        access_basic_calculator_transaction = round(trx_dict['Access Basic Calculator'],4)
    else:
        access_basic_calculator_transaction = 'NULL'
    if "Perform Basic Calculation" in trx_dict:
        perform_basic_calculation_transaction = round(trx_dict['Perform Basic Calculation'],4)
    else:
        perform_basic_calculation_transaction = 'NULL'
    if "Go Back To Home" in trx_dict:
        go_back_to_home_transaction = round(trx_dict['Go Back To Home'],4)
    else:
        go_back_to_home_transaction = 'NULL'

    current_timestamp = datetime.now(pytz.timezone('America/Los_Angeles'))

    print("We are connecting to MySQL")
    conn = mysql.connector.connect(
        user = "selenium",
        password = "Selenium#123#",
        host = "192.168.239.1",
        database="appium"
    )
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO appium_calculator
               (RunTimeStamp, Home, AccessBasicCalculator, PerformBasicCalculation, GoBackToHome)
           VALUES (%s, %s, %s, %s, %s)""",
        (current_timestamp,home_transaction,access_basic_calculator_transaction,perform_basic_calculation_transaction,go_back_to_home_transaction)
    )
    conn.commit()
    print("We have stored the results into MySQL")
    cursor.close()
    conn.close()