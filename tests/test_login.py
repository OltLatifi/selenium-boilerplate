import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        self.driver.get("https://internalpartners.mysutro.com/")
        login_page = LoginPage(self.driver)
        login_page.login("qagent", "Sutro!123")
        assert "Technician" in login_page.get_title()
