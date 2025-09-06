from playwright.sync_api import Page
import re

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_with_email_button = page.locator("button:has-text('Continue with Email')")
        self.email_input = page.locator("input#email")
        self.send_code_button = page.locator("button#btn-email")
        self.otp_input = page.locator("input#otp")
        self.verify_otp_button = page.locator("button#btn-verify")

    def start_email_login(self, email: str):
        self.continue_with_email_button.click()
        self.email_input.wait_for(state="visible")
        self.email_input.fill(email)
        self.send_code_button.click()
        self.otp_input.wait_for(state="visible", timeout=60000)

    def get_otp_from_yopmail(self, context, email: str) -> str:
        # Open new tab
        otp_tab = context.new_page()
        otp_tab.goto("https://yopmail.com/en/")

        # Enter the email
        email_address = email.split("@")[0]
        otp_tab.locator("input#login").fill(email_address)
        otp_tab.locator("i.material-icons-outlined.f36").click()

        # Wait for iframe to load
        iframe = otp_tab.frame_locator("#ifinbox")
        iframe.locator("div.m").first.wait_for(timeout=10000)
        iframe.locator("div.m").first.click()

        # Wait for message body iframe
        msg_frame = otp_tab.frame_locator("#ifmail")
        otp_text = msg_frame.locator("body").inner_text()

        # Extract OTP using regex
        otp_match = re.search(r"\b\d{4,8}\b", otp_text)
        if not otp_match:
            raise Exception("OTP not found in email content.")
        otp_code = otp_match.group(0)

        # Close the OTP tab
        otp_tab.close()

        return otp_code

    def enter_otp_and_verify(self, otp: str):
        self.otp_input.wait_for(state="visible", timeout=60000)
        self.otp_input.fill(otp)
        self.verify_otp_button.click()

