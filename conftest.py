import pytest
from datetime import datetime
from utils.driver_factory import create_android_driver
from utils.StoreToMySQL import store_transaction_result

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_name = item.name  # Extracts function name, e.g., 'test_access_currency_converter'

    # Case 1: Test failed during SETUP phase (e.g., Appium driver crashed before running test)
    if report.when == "setup" and report.failed:
        store_transaction_result(
            test_name=test_name,
            transaction="N/A",
            status="FAIL",
            duration="N/A",
            timestamp=current_timestamp
        )

    # Case 2: Test executed during CALL phase (Normal test completion or runtime failure)
    elif report.when == "call":
        status = "PASS" if report.passed else "FAIL"
        duration = f"{report.duration:.2f}s"
        transaction = getattr(item, "transaction_name", "Execution")  # Fallback transaction name

        store_transaction_result(
            test_name=test_name,
            transaction=transaction,
            status=status,
            duration=duration,
            timestamp=current_timestamp
        )

TIMEOUT = 30
@pytest.fixture(scope="session")
def driver():
    driver = create_android_driver()
    yield driver
    # 1. Close the app if it's running
    try:
        driver.terminate_app("calculator.currencyconverter.tipcalculator.unitconverter")
    except Exception:
        pass

    # 2. Force-stop the app (more reliable on Android 17)
    try:
        driver.execute_script(
            "mobile: shell",
            {
                "command": "am",
                "args": ["force-stop", "calculator.currencyconverter.tipcalculator.unitconverter"]
            }
        )
    except Exception:
        pass

    # 3. Quit the Appium session
    try:
        driver.quit()
    except Exception:
        pass
