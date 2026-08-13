import os
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):

    # ============================================================
    # NATIVE LOCATORS
    # ============================================================

    TEST_AD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Test Ad")'
    )

    LANGUAGE_HEADER = (
        AppiumBy.ID,
        "calculator.currencyconverter.tipcalculator.unitconverter:id/tvTitle"
    )

    IMPORTANT_UPDATE_TITLE = (
        AppiumBy.ID,
        "calculator.currencyconverter.tipcalculator.unitconverter:id/tvTitle"
    )

    NEXT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Next")'
    )

    HOME_TITLE = (
        AppiumBy.ID,
        "calculator.currencyconverter.tipcalculator.unitconverter:id/tvTitle"
    )

    # Existing native indicators retained as fallbacks.
    HOME_INDICATORS = [
        "Calculator",
        "Basic Calculator",
        "Scientific",
        "History",
        "Unit",
        "Currency",
    ]

    # ============================================================
    # WEBVIEW LOCATORS / IDENTIFIERS
    # ============================================================

    WEBVIEW = (
        AppiumBy.CLASS_NAME,
        "android.webkit.WebView"
    )

    AD_CONTAINER = (
        AppiumBy.ID,
        "adContainer"
    )

    MYS_WRAPPER = (
        AppiumBy.ID,
        "mys-wrapper"
    )

    MYS_CONTENT = (
        AppiumBy.ID,
        "mys-content"
    )

    # ============================================================
    # CONFIGURATION
    # ============================================================

    DEFAULT_WAIT = int(os.getenv("APPIUM_DEFAULT_WAIT", "10"))
    HOME_WAIT = int(os.getenv("APPIUM_HOME_WAIT", "30"))

    JENKINS = bool(
        os.getenv("JENKINS_URL")
        or os.getenv("BUILD_NUMBER")
        or os.getenv("JENKINS_HOME")
    )

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

        print()
        print("=" * 60)
        print("HOMEPAGE INITIALIZED")
        print("=" * 60)
        print(f"APPIUM_DEFAULT_WAIT = {self.DEFAULT_WAIT}")
        print(f"APPIUM_HOME_WAIT = {self.HOME_WAIT}")
        print(f"Jenkins environment detected = {self.JENKINS}")
        print()

    # ============================================================
    # GENERIC HELPERS
    # ============================================================

    def _safe_find(self, locator, timeout=2):
        """
        Safely attempt to locate an element without allowing
        NoSuchElementException / timeout exceptions to terminate
        the Home verification flow.
        """

        try:
            return WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(
                EC.presence_of_element_located(locator)
            )

        except (
            TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
            WebDriverException,
        ):
            return None

    def _safe_click(self, locator, timeout=2):
        """
        Safely click an element if it becomes available.
        """

        try:
            element = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(
                EC.element_to_be_clickable(locator)
            )

            element.click()
            return True

        except (
            TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
            WebDriverException,
        ):
            return False

    def _page_source_contains(self, text):
        """
        Check the current Appium page source for text.
        """

        try:
            source = self.driver.page_source or ""
            return text.lower() in source.lower()

        except WebDriverException:
            return False

    def _has_webview(self):
        """
        Determine whether the current native hierarchy contains
        a WebView.
        """

        try:
            webviews = self.driver.find_elements(
                AppiumBy.CLASS_NAME,
                "android.webkit.WebView"
            )

            if webviews:
                print(f"WebView detected: {len(webviews)}")
                return True

        except WebDriverException as exc:
            print(f"Unable to inspect WebView: {exc}")

        return self._page_source_contains("android.webkit.WebView")

    # ============================================================
    # TEST AD HANDLING
    # ============================================================

    def handle_test_ad(self):
        """
        Handles the Test Ad state without assuming that the ad must
        disappear from the native hierarchy.

        The latest Jenkins hierarchy shows that the ad is rendered
        inside a WebView and that the native 'Test Ad' TextView can
        remain visible while the WebView is active.

        Therefore, the presence of Test Ad alone is NOT treated as
        a fatal application-loading condition.
        """

        print("=" * 60)
        print("VERIFYING / DISMISSING TEST AD")
        print("=" * 60)

        if self.JENKINS:
            print(
                "Running under Jenkins - allowing 20 seconds "
                "for application initialization"
            )

            time.sleep(20)

        # --------------------------------------------------------
        # Check for native Test Ad indicator.
        # --------------------------------------------------------

        for attempt in range(1, 4):

            print(f"Test Ad check attempt {attempt}/3")

            ad = self._safe_find(
                self.TEST_AD,
                timeout=2
            )

            if ad is None:
                print("Test Ad not detected.")
                break

            print("Test Ad detected using text: Test Ad")

            # ----------------------------------------------------
            # Check whether this is actually the WebView ad.
            # ----------------------------------------------------

            if self._has_webview():

                print(
                    "WebView detected while Test Ad is present."
                )

                ad_container = self._safe_find(
                    self.AD_CONTAINER,
                    timeout=1
                )

                if ad_container is not None:
                    print(
                        "WebView adContainer detected."
                    )

                # Do not spend another 20-30 seconds waiting for
                # the native Test Ad TextView to disappear.
                #
                # The current hierarchy proves that the native
                # TextView can remain visible while the WebView
                # owns the screen.
                print(
                    "Test Ad is WebView-backed; continuing "
                    "without treating the native Test Ad label "
                    "as a blocking condition."
                )

                break

            print(
                "No WebView detected yet. "
                "Waiting for Test Ad state to update..."
            )

            time.sleep(2)

        print("Test Ad handling completed.")
        print()

        return True

    # ============================================================
    # LANGUAGE / ONBOARDING
    # ============================================================

    def handle_language_and_onboarding(self):
        """
        Handles first-run language/onboarding screens.

        If these screens are not present, the method returns
        successfully without delaying the test unnecessarily.
        """

        print("=" * 60)
        print("HANDLING LANGUAGE / ONBOARDING")
        print("=" * 60)

        # --------------------------------------------------------
        # Language screen
        # --------------------------------------------------------

        print("Checking for Language header")

        language_header = self._safe_find(
            self.LANGUAGE_HEADER,
            timeout=2
        )

        if language_header is not None:

            try:
                text = (language_header.text or "").strip()

            except WebDriverException:
                text = ""

            print(
                f"Language header detected"
                + (f": {text}" if text else "")
            )

        else:
            print("Language screen not detected.")

        # --------------------------------------------------------
        # Onboarding Next buttons
        # --------------------------------------------------------

        print("Processing onboarding Next buttons")

        for step in range(1, 6):

            print(
                f"Looking for Next button "
                f"(onboarding step {step})"
            )

            next_button = self._safe_find(
                self.NEXT_BUTTON,
                timeout=2
            )

            if next_button is None:
                print("Next button is no longer visible.")
                print("Onboarding appears to be complete.")
                break

            clicked = self._safe_click(
                self.NEXT_BUTTON,
                timeout=2
            )

            if clicked:
                print(
                    f"Clicked onboarding Next button "
                    f"(step {step})"
                )

                time.sleep(1)

            else:
                print(
                    "Next button was detected but could "
                    "not be clicked."
                )
                break

        print("Waiting for onboarding to finish")

        next_button = self._safe_find(
            self.NEXT_BUTTON,
            timeout=2
        )

        if next_button is None:
            print(
                "Onboarding Next button is no longer visible"
            )
        else:
            print(
                "Onboarding Next button is still visible"
            )

        print()

        return True

    # ============================================================
    # IMPORTANT UPDATE
    # ============================================================

    def handle_important_update(self):
        """
        Checks for the Important Update dialog.

        tvTitle is deliberately not accepted as proof that the
        Home screen is loaded because the application also uses
        tvTitle for other screens/dialogs.
        """

        print("=" * 60)
        print("CHECKING FOR IMPORTANT UPDATE")
        print("=" * 60)

        title = self._safe_find(
            self.IMPORTANT_UPDATE_TITLE,
            timeout=2
        )

        if title is None:
            print("Important Update dialog is not present.")
            print()
            return True

        try:
            title_text = (title.text or "").strip()
        except WebDriverException:
            title_text = ""

        print(
            f"tvTitle detected"
            + (f": '{title_text}'" if title_text else "")
        )

        # Only treat tvTitle as Important Update when its actual
        # text identifies that screen.
        if "important update" not in title_text.lower():
            print(
                "tvTitle is present but does not identify "
                "the Important Update screen."
            )
            print(
                "It will NOT be used as proof of Home or "
                "Important Update."
            )
            print()
            return True

        print("Important Update screen detected.")

        # --------------------------------------------------------
        # Look for common dismissal actions.
        # --------------------------------------------------------

        dismissal_texts = [
            "OK",
            "Got it",
            "Close",
            "Dismiss",
            "Later",
        ]

        for text in dismissal_texts:

            locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{text}")'
            )

            if self._safe_click(locator, timeout=1):
                print(
                    f"Dismissed Important Update using: {text}"
                )

                time.sleep(1)
                break

        print()
        return True

    # ============================================================
    # NATIVE HOME VERIFICATION
    # ============================================================

    def _verify_native_home(self):
        """
        Native fallback verification.

        This is intentionally stricter than simply finding tvTitle,
        because tvTitle is reused by other application screens.
        """

        print("Checking Home header locator...")

        header = self._safe_find(
            self.HOME_TITLE,
            timeout=1
        )

        if header is not None:

            try:
                header_text = (header.text or "").strip()
            except WebDriverException:
                header_text = ""

            print(
                "Home header candidate detected"
                + (
                    f": '{header_text}'"
                    if header_text
                    else ""
                )
            )

            # Do not accept an arbitrary tvTitle.
            if header_text:

                lower_text = header_text.lower()

                if (
                    "home" in lower_text
                    or "calculator" in lower_text
                ):
                    print(
                        "Native Home header positively identified."
                    )
                    return True

                print(
                    "tvTitle exists, but its text does not "
                    "identify the Home screen."
                )

        else:
            print("Home header element not found.")

        # --------------------------------------------------------
        # Check known Home indicators.
        # --------------------------------------------------------

        for indicator in self.HOME_INDICATORS:

            print(
                f"Checking Home indicator: {indicator}"
            )

            locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{indicator}")'
            )

            element = self._safe_find(
                locator,
                timeout=1
            )

            if element is not None:
                print(
                    f"Native Home indicator detected: "
                    f"{indicator}"
                )
                return True

        return False

    # ============================================================
    # WEBVIEW HOME VERIFICATION
    # ============================================================

    def _get_contexts_safely(self):
        """
        Return available Appium contexts without allowing a
        WebDriverException to terminate the test.
        """

        try:
            contexts = self.driver.contexts

            print()
            print("Available Appium contexts:")
            for context in contexts:
                print(f"  - {context}")

            return contexts

        except WebDriverException as exc:

            print(
                f"Unable to retrieve Appium contexts: {exc}"
            )

            return []

    def _switch_to_webview_context(self):
        """
        Attempt to switch from NATIVE_APP into an available
        WEBVIEW context.

        Returns the original context so it can be restored.
        """

        try:
            original_context = self.driver.current_context
        except WebDriverException:
            original_context = None

        print(
            f"Current Appium context: {original_context}"
        )

        contexts = self._get_contexts_safely()

        if not contexts:
            print("No Appium contexts available.")
            return None

        # Prefer WEBVIEW contexts.
        webview_contexts = [
            context
            for context in contexts
            if "WEBVIEW" in context.upper()
        ]

        if not webview_contexts:
            print(
                "No WEBVIEW context is currently exposed "
                "by Appium."
            )
            return None

        for context in webview_contexts:

            try:
                print(
                    f"Attempting to switch to: {context}"
                )

                self.driver.switch_to.context(context)

                print(
                    f"Successfully switched to: {context}"
                )

                return original_context

            except WebDriverException as exc:

                print(
                    f"Unable to switch to {context}: {exc}"
                )

        return None

    def _restore_context(self, original_context):
        """
        Restore the original Appium context.
        """

        if not original_context:
            return

        try:
            self.driver.switch_to.context(
                original_context
            )

            print(
                f"Restored Appium context: "
                f"{original_context}"
            )

        except WebDriverException as exc:

            print(
                f"Unable to restore Appium context "
                f"{original_context}: {exc}"
            )

    def _verify_webview_home(self):
        """
        Verify that the application has progressed beyond the
        blocking ad/onboarding state when the application is
        rendered through WebView.

        IMPORTANT:

        The current Jenkins hierarchy shows that the WebView
        contains:

            adContainer
            mys-wrapper
            mys-content
            portraitStylePVideo

        Therefore the WebView itself is evidence that the
        application has rendered its WebView content.

        We do NOT consider arbitrary advertisement content to be
        the Home screen.

        Instead, we look for known application indicators in the
        WebView DOM first. If Appium does not expose a WEBVIEW
        context, we use the native hierarchy as a diagnostic
        fallback.
        """

        print()
        print("-" * 60)
        print("WEBVIEW HOME VERIFICATION")
        print("-" * 60)

        if not self._has_webview():

            print(
                "No Android WebView detected."
            )

            return False

        original_context = self._switch_to_webview_context()

        if original_context is None:

            print(
                "Appium does not currently expose a WEBVIEW "
                "context."
            )

            print(
                "The native hierarchy confirms that a WebView "
                "is present, but DOM verification is unavailable."
            )

            return False

        try:

            # ----------------------------------------------------
            # Inspect WebView page source.
            # ----------------------------------------------------

            try:
                source = self.driver.page_source or ""
            except WebDriverException as exc:
                print(
                    f"Unable to retrieve WebView source: {exc}"
                )
                source = ""

            source_lower = source.lower()

            print(
                f"WebView source length: {len(source)}"
            )

            # ----------------------------------------------------
            # Look for application Home indicators.
            # ----------------------------------------------------

            web_home_indicators = [
                "calculator",
                "basic calculator",
                "scientific",
                "history",
                "unit",
                "currency",
            ]

            matches = []

            for indicator in web_home_indicators:

                if indicator.lower() in source_lower:
                    matches.append(indicator)

            if matches:

                print(
                    "WebView Home indicators detected:"
                )

                for match in matches:
                    print(f"  - {match}")

                print(
                    "WebView Home screen positively identified."
                )

                return True

            # ----------------------------------------------------
            # Look for common application DOM containers.
            # ----------------------------------------------------

            dom_identifiers = [
                "mys-wrapper",
                "mys-content",
            ]

            dom_matches = [
                identifier
                for identifier in dom_identifiers
                if identifier.lower() in source_lower
            ]

            if dom_matches:

                print(
                    "Application WebView containers detected:"
                )

                for identifier in dom_matches:
                    print(f"  - {identifier}")

                # Do NOT immediately call this Home.
                #
                # These containers were observed in the Jenkins
                # hierarchy while an advertisement was still
                # occupying the screen.
                #
                # We therefore require additional evidence.

            # ----------------------------------------------------
            # Detect whether the WebView is still dominated by the
            # ad.
            # ----------------------------------------------------

            ad_present = (
                "adcontainer" in source_lower
                or "portraitstylepvideo" in source_lower
            )

            if ad_present:

                print(
                    "WebView advertisement elements are still "
                    "present."
                )

            print(
                "No positive WebView Home indicator detected."
            )

            return False

        finally:

            self._restore_context(
                original_context
            )

    # ============================================================
    # COMBINED HOME VERIFICATION
    # ============================================================

    def _verify_home_once(self):
        """
        Perform one Home verification pass.

        Native verification is attempted first, followed by
        WebView-aware verification.
        """

        # --------------------------------------------------------
        # Native verification
        # --------------------------------------------------------

        if self._verify_native_home():
            return True

        # --------------------------------------------------------
        # WebView verification
        # --------------------------------------------------------

        if self._verify_webview_home():
            return True

        return False

    # ============================================================
    # ANDROID UI HIERARCHY DIAGNOSTICS
    # ============================================================

    def dump_ui_hierarchy(self):
        """
        Print the current Android UI hierarchy for diagnostics.
        """

        print()
        print("=" * 60)
        print("CURRENT ANDROID UI HIERARCHY")
        print("=" * 60)

        try:

            source = self.driver.page_source

            if source:
                print(source)

            else:
                print(
                    "Android UI hierarchy was empty."
                )

        except WebDriverException as exc:

            print(
                f"Unable to retrieve Android UI hierarchy: "
                f"{exc}"
            )

        print("=" * 60)
        print()

    # ============================================================
    # MAIN HOME VERIFICATION
    # ============================================================

    def verify_home_loaded(self):
        """
        Main Home screen verification.

        Flow:

            1. Handle Test Ad
            2. Handle Language / Onboarding
            3. Handle Important Update
            4. Verify Home

        The Home verification is deliberately WebView-aware
        because the Jenkins hierarchy shows the application's
        content rendered inside nested Android WebViews.
        """

        print()
        print("=" * 60)
        print("VERIFYING HOME SCREEN")
        print("=" * 60)

        # ========================================================
        # STEP 1
        # ========================================================

        print("[STEP 1/4] Handling Test Ad")

        try:

            self.handle_test_ad()

        except Exception as exc:

            print(
                f"Test Ad handling encountered an exception: "
                f"{exc}"
            )

            # Do not immediately fail Home verification.
            #
            # The latest hierarchy shows that the Test Ad can
            # remain visible while the WebView owns the screen.

        # ========================================================
        # STEP 2
        # ========================================================

        print("[STEP 2/4] Handling Language / Onboarding")

        try:

            self.handle_language_and_onboarding()

        except Exception as exc:

            print(
                f"Language/onboarding handling encountered "
                f"an exception: {exc}"
            )

        # ========================================================
        # STEP 3
        # ========================================================

        print("[STEP 3/4] Handling Important Update")

        try:

            self.handle_important_update()

        except Exception as exc:

            print(
                f"Important Update handling encountered "
                f"an exception: {exc}"
            )

        # ========================================================
        # STEP 4
        # ========================================================

        print("[STEP 4/4] Verifying Home screen")

        print(
            "Waiting for calculator Home screen to initialize..."
        )

        start_time = time.time()
        attempt = 0

        while True:

            attempt += 1

            elapsed = time.time() - start_time
            remaining = self.HOME_WAIT - elapsed

            if remaining <= 0:
                break

            print()
            print("-" * 60)
            print(
                f"Home verification attempt #{attempt}"
            )
            print(
                f"Elapsed: {elapsed:.1f}s | "
                f"Remaining: {remaining:.1f}s"
            )
            print("-" * 60)

            try:

                if self._verify_home_once():

                    print()
                    print("=" * 60)
                    print("HOME SCREEN VERIFIED")
                    print("=" * 60)
                    print()

                    return True

            except Exception as exc:

                print(
                    f"Home verification attempt raised "
                    f"an exception: {exc}"
                )

            print(
                "Home screen not verified yet."
            )

            # ----------------------------------------------------
            # Do not sleep for the entire remaining timeout.
            # Poll periodically.
            # ----------------------------------------------------

            sleep_time = min(3, max(0, remaining))

            if sleep_time > 0:
                time.sleep(sleep_time)

        # ========================================================
        # FINAL VERIFICATION
        # ========================================================

        print()
        print("=" * 60)
        print("HOME SCREEN FAILED TO LOAD")
        print("=" * 60)

        print()
        print(
            "Performing final Home-screen verification..."
        )

        try:

            if self._verify_home_once():

                print(
                    "Home screen verified during final check."
                )

                return True

        except Exception as exc:

            print(
                f"Final Home verification raised "
                f"an exception: {exc}"
            )

        print()
        print(
            "Home screen could not be verified."
        )

        print(
            "Dumping Android UI hierarchy "
            "for diagnostics..."
        )

        self.dump_ui_hierarchy()

        return False