import os
import sys

from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_successful_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        login_page = LoginPage(page)

        login_page.navigate()

        login_page.login(USERNAME, PASSWORD)

        assert "inventory" in page.url

        browser.close()