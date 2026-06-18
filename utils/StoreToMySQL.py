import mysql.connector
from datetime import datetime
import pytz
from dotenv import load_dotenv
import os


# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Retrieve the secrets using os.getenv()
mysql_host = os.getenv("MYSQL_URL")
mysql_username = os.getenv("MYSQL_USERNAME")
mysql_password = os.getenv("MYSQL_PASSWORD")


def store_to_mysql(trx_dict, device_info):
    print("We are inside the store_to_mysql function")

    # platformName
    print(device_info[0])
    # platformVersion
    print(device_info[1])
    # deviceModel
    print(device_info[2])
    # deviceManufacturer
    print(device_info[3])

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(trx_dict)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

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
    if "Access Tip Calculator" in trx_dict:
        access_tip_calculator_transaction = round(trx_dict['Access Tip Calculator'],4)
    else:
        access_tip_calculator_transaction = 'NULL'
    if "Perform Tip Calculation" in trx_dict:
        perform_tip_calculation_transaction = round(trx_dict['Perform Tip Calculation'],4)
    else:
        perform_tip_calculation_transaction = 'NULL'
    if "Go Back To Home" in trx_dict:
        go_back_to_home_transaction = round(trx_dict['Go Back To Home'],4)
    else:
        go_back_to_home_transaction = 'NULL'

    current_timestamp = datetime.now(pytz.timezone('America/Los_Angeles'))

    print("We are connecting to MySQL")

    conn = mysql.connector.connect(
        user = mysql_username,
        password = mysql_password,
        host = mysql_host,
        database="appium"
    )
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO appium_android_calculator
        (RunTimeStamp, Home, AccessBasicCalculator, PerformBasicCalculation, AccessTipCalculator, PerformTipCalculation, GoBackToHome, PlatformName, PlatformVersion, DeviceModel, DeviceManufacturer)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
(current_timestamp,home_transaction,access_basic_calculator_transaction,perform_basic_calculation_transaction,access_tip_calculator_transaction,perform_tip_calculation_transaction, go_back_to_home_transaction,
        device_info[0],device_info[1],device_info[2],device_info[3])
    )
    conn.commit()
    print("We have stored the results into MySQL")
    cursor.close()
    conn.close()