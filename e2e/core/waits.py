from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from e2e.core.logger import logger


class Waits:
    def __init__(self, driver,timeout=3):
        self.driver = driver
        self.timeout = timeout

    # Espera explícita para encontrar un elemento
    def wait_for_element(self, locator, description="elemento"):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
        logger.debug(f"✔ Apareció {description}")
        return element