from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width=1920
    browser.config.window_height=1080

    yield

    browser.quit()
