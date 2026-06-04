import time
import os
from contextlib import contextmanager
from datetime import datetime

trx_dict = {}

@contextmanager
def appium_transaction(name):
    start_time = time.time()
    print(f"\nStarting Transaction: {name}")
    try:
        yield
    finally:
        duration = time.time() - start_time
        print(f"Transaction {name} took {duration:.2f} seconds")
        trx_dict.update({name: duration})

def capture_error_snapshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = f"Error_Snapshots/{test_name}"
    os.makedirs(folder, exist_ok=True)
    screenshot_path = os.path.join(folder, f"error_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot: {screenshot_path}")