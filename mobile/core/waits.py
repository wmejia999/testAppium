from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Waits:
    def __init__(self, driver,timeout=3):
        self.driver = driver
        self.timeout = timeout

    # Espera explícita para encontrar un elemento
    def wait_for_element(self, locator, description="elemento"):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            print(f"✔ Apareció {description}")
            return element
        except TimeoutException:
            print(f"❌ No apareció {description} en {self.timeout} segundos")
            return None

