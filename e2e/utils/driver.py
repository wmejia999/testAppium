from appium import webdriver
from e2e.config.capabilities import get_android_options
from e2e.core.logger import logger

APPIUM_SERVER_URL = "http://localhost:4723"

def get_driver():
    try:
        options = get_android_options()
        driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        logger.exception(f"Error al iniciar Appium: {e}")
        raise
