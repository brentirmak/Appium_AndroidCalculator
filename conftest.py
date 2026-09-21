import pytest
from datetime import datetime
import subprocess

from utils.driver_factory import create_android_driver
from utils.StoreToMySQL import store_transaction_result


APP_PACKAGE = "calculator.currencyconverter.tipcalculator.unitconverter"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_name = item.name

    if report.when == "setup" and report.failed:
        store_transaction_result(
            test_name=test_name,
            transaction="N/A",
            status="FAIL",
            duration="N/A",
            timestamp=current_timestamp
        )

    elif report.when == "call":
        status = "PASS" if report.passed else "FAIL"
        duration = f"{report.duration:.2f}s"

        transaction = getattr(
            item,
            "transaction_name",
            "Execution"
        )

        store_transaction_result(
            test_name=test_name,
            transaction=transaction,
            status=status,
            duration=duration,
            timestamp=current_timestamp
        )


# ============================================================================
# DIRECT ADB APP CLEANUP
# ============================================================================

def force_stop_app():

    print("\n============================================================")
    print("ADB APP CLEANUP")
    print("============================================================")

    try:

        # ------------------------------------------------------------
        # Show connected devices
        # ------------------------------------------------------------

        result = subprocess.run(
            ["adb", "devices"],
            capture_output=True,
            text=True,
            timeout=10
        )

        print("ADB devices:")
        print(result.stdout)

        if result.returncode != 0:
            print(f"ADB devices failed: {result.stderr}")
            return

        # ------------------------------------------------------------
        # Force-stop Calculator
        # ------------------------------------------------------------

        print(f"Force-stopping: {APP_PACKAGE}")

        result = subprocess.run(
            [
                "adb",
                "shell",
                "am",
                "force-stop",
                APP_PACKAGE
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print("ADB force-stop completed successfully.")

        else:
            print(
                f"ADB force-stop FAILED "
                f"(return code {result.returncode})"
            )

            if result.stderr:
                print(f"ADB error: {result.stderr}")

    except Exception as e:

        print(f"ADB cleanup exception: {e}")


# ============================================================================
# APPIUM DRIVER
# ============================================================================

@pytest.fixture(scope="session")
def driver():

    driver = None

    try:

        print("\n============================================================")
        print("STARTING APPIUM DRIVER")
        print("============================================================")

        driver = create_android_driver()

        print("Appium driver started.")

        yield driver

    finally:

        print("\n============================================================")
        print("STARTING TEST CLEANUP")
        print("============================================================")

        # ------------------------------------------------------------
        # 1. Try Appium terminate_app()
        # ------------------------------------------------------------

        if driver is not None:

            try:

                print("Attempting Appium terminate_app()...")

                driver.terminate_app(APP_PACKAGE)

                print(
                    "Appium terminate_app() completed."
                )

            except Exception as e:

                print(
                    f"Appium terminate_app() failed: {e}"
                )

        # ------------------------------------------------------------
        # 2. DIRECT ADB FORCE-STOP
        # ------------------------------------------------------------

        force_stop_app()

        # ------------------------------------------------------------
        # 3. Quit Appium
        # ------------------------------------------------------------

        if driver is not None:

            try:

                print("Closing Appium session...")

                driver.quit()

                print(
                    "Appium session closed successfully."
                )

            except Exception as e:

                print(
                    f"Appium driver.quit() failed: {e}"
                )

        print("\n============================================================")
        print("TEST CLEANUP COMPLETED")
        print("============================================================")