import pytest
from utils.driver_factory import create_android_driver

# Shared container so pytest_sessionfinish can access device_info
collected_device_info = []

TIMEOUT = 10

@pytest.fixture
def driver():
    driver = create_android_driver()
    yield driver
    driver.quit()