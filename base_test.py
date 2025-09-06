from playwright.sync_api import sync_playwright

class BaseTest:
    def setup_method(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
        headless=False,
        slow_mo=300,
        args=["--start-maximized"]
        )

        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()

    def teardown_method(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
