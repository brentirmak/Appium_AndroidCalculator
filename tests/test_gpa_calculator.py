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
            is_displayed, page_title = gpa_calculator_page.verify_loaded()

            assert is_displayed, "GPA Calculator header is not displayed"
            assert page_title == "GPA Calculator", f"Expected page title 'GPA Calculator' but found '{page_title}'"
        except Exception:
            capture_error_snapshot(driver, "AccessGPACalculator")
            raise

@pytest.mark.timeout(175)
def test_list_cleanup(driver):
    gpa_calculator_page = GPACalculatorPage(driver)

    with appium_transaction("List Cleanup"):
        try:
            subject_exists = True
            while subject_exists:
                print("Will verify that there's a subject entry in the list")
                record_exists = gpa_calculator_page.verify_top_course_entry()
                print("Record exists: ", record_exists)
                if record_exists:
                    print("A record exits - will proceed with deleting the subject")
                    gpa_calculator_page.delete_top_subject()
                else:
                    gpa_calculator_page.verify_no_data()
                    subject_exists = False
                    print("There are no records to be deleted")
        except Exception:
            capture_error_snapshot(driver, "ListCleanup")
            raise


@pytest.mark.timeout(175)
def test_add_subject_to_list(driver):
    gpa_calculator_page = GPACalculatorPage(driver)

    with appium_transaction("Add Subjects To List"):
        try:
            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('MATH', 3, 92)
            print("Subject has been added to list")

            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('PE', 2, 95)
            print("Subject has been added to list")

            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('ENGLISH', 4, 88)
            print("Subject has been added to list")

            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('HISTORY', 3, 80)
            print("Subject has been added to list")

            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('FRENCH', 2, 94)
            print("Subject has been added to list")

            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('SCIENCE', 3, 83)
            print("Subject has been added to list")

            print("Will click on the Click Add a Subject button")
            gpa_calculator_page.click_add_a_subject_button()
            print("Accessed Add a Subject screen")

            print("Will add a subject to list")
            gpa_calculator_page.enter_subject_details('GEOGRAPHY', 3, 97)
            print("Subject has been added to list")

            total_credits, total_gpa = gpa_calculator_page.capture_total_credit()

            assert total_credits == "20.00", f"Expected 20.00 but got {total_credits}"
            assert total_gpa == "89.30", f"Expected 89.30 but got {total_gpa}"
        except Exception:
            capture_error_snapshot(driver, "AddSubjectsToList")
            raise

@pytest.mark.timeout(175)
def test_delete_subject_from_list(driver):
    gpa_calculator_page = GPACalculatorPage(driver)

    with appium_transaction("Delete Subjects From List"):
        try:
            subject_exists = True
            while subject_exists:
                print("Will verify that there's a subject entry in the list")
                record_exists = gpa_calculator_page.verify_top_course_entry()
                print("Record exists: ", record_exists)
                if record_exists:
                    print("A record exits - will proceed with deleting the subject")
                    gpa_calculator_page.delete_top_subject()
                else:
                    gpa_calculator_page.verify_no_data()
                    subject_exists = False
                    print("There are no records to be deleted")

        except Exception:
            capture_error_snapshot(driver, "DeleteSubjectsFromList")
            raise
