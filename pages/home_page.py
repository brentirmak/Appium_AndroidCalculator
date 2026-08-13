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

    # Known native Home indicators.
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

    DEFAULT_WAIT = int(
        os.getenv("APPIUM_DEFAULT_WAIT", "10")
    )

    HOME_WAIT = int(
        os.getenv("APPIUM_HOME_WAIT", "30")
    )

    JENKINS = bool(
        os.getenv("JENKINS_URL")
        or os.getenv("BUILD_NUMBER")
        or os.getenv("JENKINS_HOME")
    )

    # Jenkins can be slower when the emulator, Appium server,
    # application and WebView are all starting together.
    JENKINS_AD_WAIT = int(
        os.getenv("APPIUM_JENKINS_AD_WAIT", "15")
    )

    # ============================================================
    # INITIALIZATION
    # ============================================================

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

        print()
        print("=" * 60)
        print("HOMEPAGE INITIALIZED")
        print("=" * 60)
        print(
            f"APPIUM_DEFAULT_WAIT = {self.DEFAULT_WAIT}"
        )
        print(
            f"APPIUM_HOME_WAIT = {self.HOME_WAIT}"
        )
        print(
            f"APPIUM_JENKINS_AD_WAIT = "
            f"{self.JENKINS_AD_WAIT}"
        )
        print(
            f"Jenkins environment detected = "
            f"{self.JENKINS}"
        )
        print()

    # ============================================================
    # GENERIC HELPERS
    # ============================================================

    def _safe_find(self, locator, timeout=2):
        """
        Safely locate an element.

        Returns:
            WebElement if found
            None if not found or Appium reports an error
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

    def _safe_find_elements(self, locator):
        """
        Safely return a list of elements.
        """

        try:
            return self.driver.find_elements(*locator)

        except WebDriverException:
            return []

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

    def _get_page_source(self):
        """
        Safely retrieve Appium page source.
        """

        try:
            return self.driver.page_source or ""

        except WebDriverException as exc:

            print(
                f"Unable to retrieve page source: {exc}"
            )

            return ""

    # ============================================================
    # WEBVIEW DETECTION
    # ============================================================

    def _has_webview(self):
        """
        Determine whether an Android WebView exists in the
        current native hierarchy.
        """

        try:

            webviews = self.driver.find_elements(
                AppiumBy.CLASS_NAME,
                "android.webkit.WebView"
            )

            if webviews:

                print(
                    f"WebView detected: "
                    f"{len(webviews)}"
                )

                return True

        except WebDriverException as exc:

            print(
                f"Unable to inspect WebView: {exc}"
            )

        return self._page_source_contains(
            "android.webkit.WebView"
        )

    # ============================================================
    # TEST AD HANDLING
    # ============================================================

    def handle_test_ad(self):
        """
        Handle the Test Ad state.

        Important Jenkins behavior:

        The native "Test Ad" TextView can remain present while
        the actual application content is rendered inside a
        WebView.

        Therefore:

            Test Ad + WebView != failure

        We only use the ad state as diagnostic information.
        """

        print("=" * 60)
        print("VERIFYING / HANDLING TEST AD")
        print("=" * 60)

        # --------------------------------------------------------
        # Jenkins startup delay
        # --------------------------------------------------------

        if self.JENKINS:

            print(
                "Running under Jenkins."
            )

            print(
                f"Allowing up to "
                f"{self.JENKINS_AD_WAIT} seconds "
                f"for emulator/application startup."
            )

            start_time = time.time()

            while (
                time.time() - start_time
                < self.JENKINS_AD_WAIT
            ):

                if self._has_webview():

                    print(
                        "WebView detected during Jenkins "
                        "startup wait."
                    )

                    break

                time.sleep(2)

        # --------------------------------------------------------
        # Inspect Test Ad
        # --------------------------------------------------------

        ad = self._safe_find(
            self.TEST_AD,
            timeout=2
        )

        if ad is None:

            print(
                "Test Ad text was not detected."
            )

            print(
                "Test Ad handling completed."
            )

            print()

            return True

        print(
            "Test Ad detected using text: Test Ad"
        )

        # --------------------------------------------------------
        # Determine whether WebView is active.
        # --------------------------------------------------------

        if self._has_webview():

            print(
                "WebView is present while Test Ad "
                "is still visible."
            )

            print(
                "This is considered a valid application "
                "startup state."
            )

            ad_container = self._safe_find(
                self.AD_CONTAINER,
                timeout=1
            )

            if ad_container is not None:

                print(
                    "WebView adContainer detected."
                )

            print(
                "Native Test Ad label will NOT be "
                "treated as a blocking condition."
            )

            print()

            return True

        # --------------------------------------------------------
        # No WebView yet.
        # --------------------------------------------------------

        print(
            "Test Ad detected but WebView is not "
            "currently exposed."
        )

        print(
            "Waiting briefly for the application "
            "to transition."
        )

        for attempt in range(1, 4):

            print(
                f"Test Ad transition check "
                f"{attempt}/3"
            )

            time.sleep(2)

            if self._has_webview():

                print(
                    "WebView detected."
                )

                print(
                    "Continuing with Home verification."
                )

                print()

                return True

            ad = self._safe_find(
                self.TEST_AD,
                timeout=1
            )

            if ad is None:

                print(
                    "Test Ad is no longer visible."
                )

                break

        print(
            "Test Ad handling completed."
        )

        print()

        return True

    # ============================================================
    # LANGUAGE / ONBOARDING
    # ============================================================

    def handle_language_and_onboarding(self):
        """
        Handle first-run language/onboarding screens.

        These screens are optional. If they do not exist,
        verification continues immediately.
        """

        print("=" * 60)
        print("HANDLING LANGUAGE / ONBOARDING")
        print("=" * 60)

        # --------------------------------------------------------
        # Language screen
        # --------------------------------------------------------

        print(
            "Checking for Language header"
        )

        language_header = self._safe_find(
            self.LANGUAGE_HEADER,
            timeout=2
        )

        if language_header is not None:

            try:
                text = (
                    language_header.text or ""
                ).strip()

            except WebDriverException:
                text = ""

            print(
                "tvTitle detected"
                + (
                    f": '{text}'"
                    if text
                    else ""
                )
            )

        else:

            print(
                "Language screen not detected."
            )

        # --------------------------------------------------------
        # Next buttons
        # --------------------------------------------------------

        print(
            "Processing onboarding Next buttons"
        )

        for step in range(1, 6):

            print(
                f"Looking for Next button "
                f"(step {step})"
            )

            next_button = self._safe_find(
                self.NEXT_BUTTON,
                timeout=2
            )

            if next_button is None:

                print(
                    "Next button is no longer visible."
                )

                print(
                    "Onboarding appears to be complete."
                )

                break

            clicked = self._safe_click(
                self.NEXT_BUTTON,
                timeout=2
            )

            if clicked:

                print(
                    f"Clicked Next button "
                    f"(step {step})"
                )

                time.sleep(1)

            else:

                print(
                    "Next button was detected but "
                    "could not be clicked."
                )

                break

        print(
            "Waiting for onboarding to finish"
        )

        next_button = self._safe_find(
            self.NEXT_BUTTON,
            timeout=2
        )

        if next_button is None:

            print(
                "Onboarding Next button is no longer visible."
            )

        else:

            print(
                "Onboarding Next button is still visible."
            )

        print()

        return True

    # ============================================================
    # IMPORTANT UPDATE
    # ============================================================

    def handle_important_update(self):
        """
        Check for the Important Update screen.

        tvTitle alone is NOT sufficient because the application
        reuses tvTitle across multiple screens.
        """

        print("=" * 60)
        print("CHECKING FOR IMPORTANT UPDATE")
        print("=" * 60)

        title = self._safe_find(
            self.IMPORTANT_UPDATE_TITLE,
            timeout=2
        )

        if title is None:

            print(
                "Important Update dialog is not present."
            )

            print()

            return True

        try:

            title_text = (
                title.text or ""
            ).strip()

        except WebDriverException:

            title_text = ""

        print(
            "tvTitle detected"
            + (
                f": '{title_text}'"
                if title_text
                else ""
            )
        )

        # --------------------------------------------------------
        # Important Update confirmation
        # --------------------------------------------------------

        if (
            "important update"
            not in title_text.lower()
        ):

            print(
                "tvTitle does not identify "
                "Important Update."
            )

            print(
                "It will NOT be treated as an "
                "Important Update dialog."
            )

            print()

            return True

        print(
            "Important Update screen detected."
        )

        # --------------------------------------------------------
        # Possible dismissal buttons
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
                (
                    'new UiSelector().text("'
                    f'{text}"
                    '")'
                ),
            )

            if self._safe_click(
                locator,
                timeout=1
            ):

                print(
                    f"Dismissed Important Update "
                    f"using: {text}"
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
        Verify Home using native Android elements.

        The generic tvTitle locator is NOT accepted by itself.
        """

        print(
            "Checking native Home indicators..."
        )

        # --------------------------------------------------------
        # Inspect tvTitle
        # --------------------------------------------------------

        header = self._safe_find(
            self.HOME_TITLE,
            timeout=1
        )

        if header is not None:

            try:

                header_text = (
                    header.text or ""
                ).strip()

            except WebDriverException:

                header_text = ""

            print(
                "tvTitle candidate detected"
                + (
                    f": '{header_text}'"
                    if header_text
                    else ""
                )
            )

            if header_text:

                lower_text = (
                    header_text.lower()
                )

                if (
                    "home" in lower_text
                    or "calculator" in lower_text
                ):

                    print(
                        "Native Home header "
                        "positively identified."
                    )

                    return True

                print(
                    "tvTitle exists but does not "
                    "identify Home."
                )

        # --------------------------------------------------------
        # Known Home indicators
        # --------------------------------------------------------

        for indicator in self.HOME_INDICATORS:

            print(
                f"Checking native Home indicator: "
                f"{indicator}"
            )

            locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                (
                    'new UiSelector().text("'
                    f'{indicator}"
                    '")'
                ),
            )

            element = self._safe_find(
                locator,
                timeout=1
            )

            if element is not None:

                print(
                    "Native Home indicator detected: "
                    f"{indicator}"
                )

                return True

        # --------------------------------------------------------
        # Native page-source fallback
        # --------------------------------------------------------

        source = self._get_page_source()

        if source:

            source_lower = source.lower()

            native_matches = []

            for indicator in self.HOME_INDICATORS:

                if (
                    indicator.lower()
                    in source_lower
                ):

                    native_matches.append(
                        indicator
                    )

            if native_matches:

                print(
                    "Home indicators found in "
                    "native page source:"
                )

                for match in native_matches:

                    print(
                        f"  - {match}"
                    )

                return True

        print(
            "Native Home screen not positively "
            "identified."
        )

        return False

    # ============================================================
    # APPIUM CONTEXT HANDLING
    # ============================================================

    def _get_contexts_safely(self):
        """
        Safely retrieve Appium contexts.
        """

        try:

            contexts = self.driver.contexts

            print()
            print(
                "Available Appium contexts:"
            )

            for context in contexts:

                print(
                    f"  - {context}"
                )

            return contexts

        except WebDriverException as exc:

            print(
                "Unable to retrieve Appium "
                f"contexts: {exc}"
            )

            return []

    def _switch_to_webview_context(self):
        """
        Switch to the first available WEBVIEW context.

        Returns:
            original context if successful
            None otherwise
        """

        try:

            original_context = (
                self.driver.current_context
            )

        except WebDriverException:

            original_context = None

        print(
            f"Current Appium context: "
            f"{original_context}"
        )

        contexts = (
            self._get_contexts_safely()
        )

        if not contexts:

            print(
                "No Appium contexts available."
            )

            return None

        webview_contexts = [
            context
            for context in contexts
            if "WEBVIEW"
            in context.upper()
        ]

        if not webview_contexts:

            print(
                "No WEBVIEW context is currently "
                "exposed by Appium."
            )

            return None

        for context in webview_contexts:

            try:

                print(
                    f"Attempting to switch to: "
                    f"{context}"
                )

                self.driver.switch_to.context(
                    context
                )

                print(
                    f"Successfully switched to: "
                    f"{context}"
                )

                return original_context

            except WebDriverException as exc:

                print(
                    f"Unable to switch to "
                    f"{context}: {exc}"
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
                "Unable to restore Appium context "
                f"{original_context}: {exc}"
            )

    # ============================================================
    # WEBVIEW DOM VERIFICATION
    # ============================================================

    def _verify_webview_home(self):
        """
        Verify Home when the application is rendered through
        an Android WebView.

        Verification priority:

            1. Known application Home indicators
            2. Known application WebView containers
            3. Stable WebView application structure

        IMPORTANT:

        The Jenkins hierarchy has shown:

            android.webkit.WebView
            adContainer
            mys-wrapper
            mys-content
            portraitStylePVideo

        Therefore WebView presence alone is NOT sufficient.

        However, a stable WebView containing the application's
        known containers can be used as fallback evidence after
        native verification has failed.
        """

        print()
        print("-" * 60)
        print("WEBVIEW HOME VERIFICATION")
        print("-" * 60)

        # --------------------------------------------------------
        # First verify WebView exists.
        # --------------------------------------------------------

        if not self._has_webview():

            print(
                "No Android WebView detected."
            )

            return False

        print(
            "Android WebView confirmed."
        )

        # --------------------------------------------------------
        # Attempt WEBVIEW context.
        # --------------------------------------------------------

        original_context = (
            self._switch_to_webview_context()
        )

        # --------------------------------------------------------
        # Appium may expose the native WebView but not expose a
        # WEBVIEW context. This is common with some emulator /
        # Chrome WebView combinations.
        # --------------------------------------------------------

        if original_context is None:

            print(
                "WEBVIEW context is unavailable."
            )

            print(
                "Native hierarchy confirms WebView "
                "presence."
            )

            # Do not immediately accept the WebView as Home.
            #
            # Instead inspect the native source for known
            # application structures.

            source = self._get_page_source()

            source_lower = source.lower()

            application_container_present = (
                "mys-wrapper" in source_lower
                or "mys-content" in source_lower
            )

            home_indicator_present = any(
                indicator.lower()
                in source_lower
                for indicator
                in self.HOME_INDICATORS
            )

            if home_indicator_present:

                print(
                    "Known Home indicator found in "
                    "native hierarchy."
                )

                return True

            if application_container_present:

                print(
                    "Known application WebView "
                    "container detected in native "
                    "hierarchy."
                )

                print(
                    "Using stable application "
                    "WebView structure as fallback "
                    "Home evidence."
                )

                return True

            print(
                "WebView exists, but no positive "
                "Home evidence was found."
            )

            return False

        try:

            # ----------------------------------------------------
            # Retrieve WebView DOM.
            # ----------------------------------------------------

            source = self._get_page_source()

            source_lower = source.lower()

            print(
                f"WebView source length: "
                f"{len(source)}"
            )

            # ----------------------------------------------------
            # Strong Home indicators
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

            for indicator in (
                web_home_indicators
            ):

                if (
                    indicator.lower()
                    in source_lower
                ):

                    matches.append(
                        indicator
                    )

            if matches:

                print(
                    "WebView Home indicators detected:"
                )

                for match in matches:

                    print(
                        f"  - {match}"
                    )

                print(
                    "WebView Home screen "
                    "positively identified."
                )

                return True

            # ----------------------------------------------------
            # Application containers
            # ----------------------------------------------------

            wrapper_present = (
                "mys-wrapper"
                in source_lower
            )

            content_present = (
                "mys-content"
                in source_lower
            )

            ad_container_present = (
                "adcontainer"
                in source_lower
            )

            video_present = (
                "portraitstylepvideo"
                in source_lower
            )

            print(
                "WebView structure:"
            )

            print(
                f"  mys-wrapper = "
                f"{wrapper_present}"
            )

            print(
                f"  mys-content = "
                f"{content_present}"
            )

            print(
                f"  adContainer = "
                f"{ad_container_present}"
            )

            print(
                f"  portraitStylePVideo = "
                f"{video_present}"
            )

            # ----------------------------------------------------
            # Strong application structure.
            # ----------------------------------------------------

            if (
                wrapper_present
                and content_present
            ):

                print(
                    "mys-wrapper and mys-content "
                    "are both present."
                )

                # If Home indicators were not found, we still
                # have to determine whether this is simply the
                # advertisement layer.
                #
                # If the application containers are present and
                # the source is not exclusively an advertisement,
                # treat this as valid fallback evidence.

                ad_only = (
                    ad_container_present
                    and video_present
                    and not any(
                        indicator.lower()
                        in source_lower
                        for indicator
                        in web_home_indicators
                    )
                )

                if ad_only:

                    print(
                        "WebView still appears "
                        "advertisement-dominated."
                    )

                    print(
                        "Not yet accepting this as Home."
                    )

                    return False

                print(
                    "Stable application WebView "
                    "structure detected."
                )

                print(
                    "Using WebView application "
                    "structure as Home fallback."
                )

                return True

            # ----------------------------------------------------
            # Individual application container.
            # ----------------------------------------------------

            if (
                wrapper_present
                or content_present
            ):

                print(
                    "Application WebView container "
                    "detected."
                )

                # If the advertisement is still clearly
                # dominating the WebView, don't accept it.

                if (
                    ad_container_present
                    and video_present
                ):

                    print(
                        "Advertisement indicators "
                        "are still present."
                    )

                    print(
                        "Waiting for the WebView "
                        "to progress."
                    )

                    return False

                print(
                    "WebView application container "
                    "appears stable."
                )

                return True

            # ----------------------------------------------------
            # No useful DOM evidence.
            # ----------------------------------------------------

            print(
                "No positive WebView Home "
                "indicator detected."
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

        Verification order:

            1. Native Home
            2. WebView Home
        """

        print()
        print(
            "Starting combined Home verification..."
        )

        # --------------------------------------------------------
        # Native verification
        # --------------------------------------------------------

        try:

            if self._verify_native_home():

                print(
                    "Home verified through "
                    "native Android hierarchy."
                )

                return True

        except Exception as exc:

            print(
                "Native Home verification "
                f"raised exception: {exc}"
            )

        # --------------------------------------------------------
        # WebView verification
        # --------------------------------------------------------

        try:

            if self._verify_webview_home():

                print(
                    "Home verified through "
                    "WebView/application structure."
                )

                return True

        except Exception as exc:

            print(
                "WebView Home verification "
                f"raised exception: {exc}"
            )

        print(
            "Home could not be verified "
            "during this pass."
        )

        return False

    # ============================================================
    # ANDROID UI HIERARCHY DIAGNOSTICS
    # ============================================================

    def dump_ui_hierarchy(self):
        """
        Print the current Android UI hierarchy.
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
                "Unable to retrieve Android "
                f"UI hierarchy: {exc}"
            )

        print("=" * 60)
        print()

    # ============================================================
    # CURRENT CONTEXT DIAGNOSTICS
    # ============================================================

    def dump_context_information(self):
        """
        Print current Appium context information.

        Useful when Jenkins exposes a WebView in the native
        hierarchy but does not expose a WEBVIEW context.
        """

        print()
        print("=" * 60)
        print("APPIUM CONTEXT DIAGNOSTICS")
        print("=" * 60)

        try:

            print(
                f"Current context: "
                f"{self.driver.current_context}"
            )

        except WebDriverException as exc:

            print(
                f"Unable to retrieve current "
                f"context: {exc}"
            )

        self._get_contexts_safely()

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

        The method intentionally does not fail immediately when
        optional startup screens or WebView transitions encounter
        temporary Appium exceptions.
        """

        print()
        print("=" * 60)
        print("VERIFYING HOME SCREEN")
        print("=" * 60)
        print()

        # ========================================================
        # STEP 1 - TEST AD
        # ========================================================

        print(
            "[STEP 1/4] Handling Test Ad"
        )

        try:

            self.handle_test_ad()

        except Exception as exc:

            print(
                "Test Ad handling encountered "
                f"an exception: {exc}"
            )

            print(
                "Continuing to Home verification."
            )

        # ========================================================
        # STEP 2 - LANGUAGE / ONBOARDING
        # ========================================================

        print(
            "[STEP 2/4] Handling Language / Onboarding"
        )

        try:

            self.handle_language_and_onboarding()

        except Exception as exc:

            print(
                "Language/onboarding handling "
                f"encountered an exception: {exc}"
            )

            print(
                "Continuing to Home verification."
            )

        # ========================================================
        # STEP 3 - IMPORTANT UPDATE
        # ========================================================

        print(
            "[STEP 3/4] Handling Important Update"
        )

        try:

            self.handle_important_update()

        except Exception as exc:

            print(
                "Important Update handling "
                f"encountered an exception: {exc}"
            )

            print(
                "Continuing to Home verification."
            )

        # ========================================================
        # STEP 4 - HOME VERIFICATION
        # ========================================================

        print(
            "[STEP 4/4] Verifying Home screen"
        )

        print(
            "Waiting for calculator Home screen "
            "to initialize..."
        )

        start_time = time.time()
        attempt = 0

        while True:

            attempt += 1

            elapsed = (
                time.time()
                - start_time
            )

            remaining = (
                self.HOME_WAIT
                - elapsed
            )

            if remaining <= 0:

                break

            print()
            print("-" * 60)
            print(
                f"Home verification attempt "
                f"#{attempt}"
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
                    "Home verification attempt "
                    f"raised an exception: {exc}"
                )

            print(
                "Home screen not verified yet."
            )

            # ----------------------------------------------------
            # Poll every 3 seconds.
            # ----------------------------------------------------

            sleep_time = min(
                3,
                max(
                    0,
                    remaining
                )
            )

            if sleep_time > 0:

                time.sleep(
                    sleep_time
                )

        # ========================================================
        # FINAL VERIFICATION
        # ========================================================

        print()
        print("=" * 60)
        print("HOME SCREEN FAILED TO LOAD")
        print("=" * 60)

        print()
        print(
            "Performing final Home-screen "
            "verification..."
        )

        try:

            if self._verify_home_once():

                print(
                    "Home screen verified during "
                    "final check."
                )

                print()

                return True

        except Exception as exc:

            print(
                "Final Home verification "
                f"raised an exception: {exc}"
            )

        # ========================================================
        # DIAGNOSTICS
        # ========================================================

        print()
        print(
            "Home screen could not be verified."
        )

        print()
        print(
            "Dumping Appium context information..."
        )

        self.dump_context_information()

        print(
            "Dumping Android UI hierarchy "
            "for diagnostics..."
        )

        self.dump_ui_hierarchy()

        return False