import time
import os
from datetime import datetime
from utils.StoreToMySQL import store_transaction_result

def appium_transaction(name):
    class TransactionContext:
        def __enter__(self):
            print(f"Starting transaction: {name}")
            self.start_time = time.time()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            duration = round(time.time() - self.start_time, 2)
            status = "PASS" if exc_type is None else "FAIL"

            print(f"Ending transaction: {name} | Status: {status} | Duration: {duration}s")

            # Log to MySQL
            store_transaction_result(
                transaction=name,
                status=status,
                duration=duration,
                timestamp=datetime.now()
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
