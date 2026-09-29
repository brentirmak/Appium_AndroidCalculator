import logging
import os
from contextlib import contextmanager

import pytest

from pages.home_page import HomePage
from pages.ai_calculator_page import AICalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

log = logging.getLogger(__name__)

# Per-test hard timeouts get more headroom under Jenkins (override with CI_TIMEOUT_FACTOR)
CI_TIMEOUT_FACTOR = float(os.getenv("CI_TIMEOUT_FACTOR", "1.5" if os.getenv("JENKINS_URL") else "1"))


def _t(seconds):
    return int(seconds * CI_TIMEOUT_FACTOR)


@contextmanager
def snapshot_on_failure(driver, name):
    """Replaces the repeated try/except + capture_error_snapshot blocks in every test."""
    try:
        yield
    except Exception:
        try:
            capture_error_snapshot(driver, name)
        except Exception:
            log.exception("capture_error_snapshot failed - original error follows")
        raise


@pytest.mark.timeout(_t(180))
def test_access_date_calculator(driver):
    home = HomePage(driver)
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Access Date Calculator"), snapshot_on_failure(driver, "AccessDateCalculator"):
        assert home.load_landing_page(), "Not at Home screen"

        ai_calculator.open_from_home()
        page_header = ai_calculator.verify_loaded()
        assert "AI Scan" in page_header, f"AI Scan header not found. Got: '{page_header}'"


@pytest.mark.timeout(_t(180))
def test_clear_chat_history(driver):
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Clear Chat History"), snapshot_on_failure(driver, "ClearChatHistory"):
        ai_calculator.ensure_on_ai_scan_screen()
        ai_calculator.access_ai_chat_screen()
        ai_calculator.clear_chat_history()


@pytest.mark.timeout(_t(180))
def test_perform_ai_chat_calculation(driver):
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Perform AI Chat Calculation"), snapshot_on_failure(driver, "PerformAIChatCalculation"):
        ai_calculator.ensure_on_ai_scan_screen()
        ai_calculator.access_ai_chat_screen()
        simple_addition_result = ai_calculator.perform_simple_addition()
        print("Simple addition result is :", simple_addition_result)
        assert "4" in simple_addition_result, f"Expected 4 but got {simple_addition_result}"


@pytest.mark.timeout(_t(240))
def test_perform_2nd_ai_chat_calculation(driver):
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Perform 2nd AI Chat Calculation"), snapshot_on_failure(driver, "Perform2ndAIChatCalculation"):
        # State-aware: works whether the previous test left us in chat, history, or home
        ai_calculator.ensure_on_ai_scan_screen()
        ai_calculator.access_ai_chat_screen()
        ai_calculator.clear_chat_history()

        simple_subtraction_result = ai_calculator.perform_simple_subtraction()
        print("Simple subtraction result is :", simple_subtraction_result)
        assert "10" in simple_subtraction_result, f"Expected 10 but got {simple_subtraction_result}"