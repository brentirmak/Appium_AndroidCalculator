import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.gpa_calculator_page import GPACalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_gpa_calculator(driver):
    side_menu = SideMenuPage(driver)
    gpa_calculator_page = GPACalculatorPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access GPA Calculator"):
        print("Checking to see if we're at Home screen")
        if not home.load_landing_page():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for GPA Calculator")
            side_menu.click_gpa_calculator()
            assert gpa_calculator_page.verify_loaded(), "GPA Calculator header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessGPACalculator")
            raise


@pytest.mark.timeout(175)
def test_add_subject_to_list(driver):
    gpa_calculator_page = GPACalculatorPage(driver)

    with appium_transaction("Add Subject To List"):
        try:
            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")
            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details()
            print("Subject has been added to list")
            #assert output == "4.3307", f"Expected 4.3307 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "AddSubjectToList")
            raise

@pytest.mark.timeout(175)
def test_delete_subject_from_list(driver):
    gpa_calculator_page = GPACalculatorPage(driver)

    with appium_transaction("Delete Subject From List"):
        try:
            print("Will verify that there's a subject entry in the list")
            record_exists = gpa_calculator_page.verify_top_course_entry()
            print("Record exists: ", record_exists)
            if record_exists:
                print("A record exits - will proceed with deleting the subject")
                gpa_calculator_page.delete_top_subject()
            else:
                gpa_calculator_page.verify_no_data()
                print("There were no records to be deleted")

        except Exception:
            capture_error_snapshot(driver, "DeleteSubjectFromList")
            raise