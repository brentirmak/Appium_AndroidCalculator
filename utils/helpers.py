import inspect
import os
import time
from datetime import datetime
from utils.StoreToMySQL import store_transaction_result


def appium_transaction(name, test_name=None):
    # Automatically capture the filename of the caller if test_name is not provided
    if test_name is None:
        caller_frame = inspect.stack()[1]
        test_name = os.path.basename(caller_frame.filename)

    class TransactionContext:

        def __enter__(self):
            print(f"\nStarting transaction: {name} (Test: {test_name})")
            self.start_time = time.time()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            duration = round(time.time() - self.start_time, 2)
            status = "PASS" if exc_type is None else "FAIL"

            print(
                f"Ending transaction: {name} | Status: {status} | Duration: {duration}s"
            )

            # Log to MySQL with test_name included
            store_transaction_result(
                test_name=test_name,
                transaction=name,
                status=status,
                duration=duration,
                timestamp=datetime.now(),
            )

            return False  # rethrow exceptions if any

    return TransactionContext()


def capture_error_snapshot(driver, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"error_{name}_{timestamp}.png"
    path = os.path.join("snapshots", filename)

    os.makedirs("snapshots", exist_ok=True)
    driver.save_screenshot(path)

    print(f"Saved error snapshot: {path}")