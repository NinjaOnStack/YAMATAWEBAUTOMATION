import re
from playwright.sync_api import BrowserContext

class YopmailPage:
    def __init__(self, context):
        self.context = context

    def get_otp_from_yopmail(self, email_prefix: str) -> str:
        # Open Yopmail in a new tab
        page = self.context.new_page()
        page.goto("https://yopmail.com/en/")

        # Fill email and check inbox
        page.fill("#login", email_prefix)
        page.keyboard.press("Enter")

        # Wait for the iframe to load and switch into it
        page.frame_locator("#ifinbox").locator("text=Yamata").first.click()

        # Wait for the email to load in right iframe
        email_frame = page.frame(name="ifmail")
        email_frame.wait_for_selector("text=Your verification code is:")

        # Extract the OTP
        otp_text = email_frame.locator("text=Your verification code is:").text_content()
        otp = otp_text.strip().split()[-1]  # Grabs the last word which is the OTP

        page.close()  # Close Yopmail tab
        return otp
