import json
from pathlib import Path
from base_test import BaseTest
from pages.login_page import LoginPage
from pages.yopmail_page import YopmailPage
from playwright.sync_api import expect

def load_test_data():
    file_path = Path(__file__).parent.parent / "test_data" / "LoginTestData.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_config():
    config_path = Path(__file__).parent.parent / "config" / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

class TestLogin(BaseTest):

    def test_valid_login(self):
        test_data = load_test_data()
        config = load_config()

        email = test_data["User"]["email"]
        email_prefix = email.split("@")[0]
        base_url = config["base_url"]

        self.page.goto(base_url)

        login_page = LoginPage(self.page)
        login_page.start_email_login(email)

        yopmail_page = YopmailPage(self.context)
        otp = yopmail_page.get_otp_from_yopmail(email_prefix)

        login_page.enter_otp_and_verify(otp)

        expect(self.page.locator("a[href='/dashboard']:has-text('Dashboard')")).to_be_visible()

    def test_invalid_otp_login(self):
        test_data = load_test_data()
        config = load_config()

        email = test_data["User"]["email"]
        base_url = config["base_url"]

        self.page.goto(base_url)

        login_page = LoginPage(self.page)
        login_page.start_email_login(email)

        invalid_otp = "000000"
        login_page.enter_otp_and_verify(invalid_otp)

        expect(self.page.locator("#error-message-otp")).to_be_visible()
        expect(self.page.locator("#error-message-otp")).to_have_text("Wrong email or verification code.")