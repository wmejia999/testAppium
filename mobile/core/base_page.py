from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from mobile.core.logger import logger
from mobile.core.waits import Waits

"""
Centraliza las acciones sobre los elementos.
Todas las clases heredaran está clase.
"""

class BasePage:

    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.timeout = timeout
        self.waits = Waits(driver,timeout)

    # Click genérico
    def click_element(self, locator, description="elemento"):
        try:
            print("estoy esperando...")
            element = self.waits.wait_for_element(locator,description)
            element.click()
            self._log_action("ok", description)

        except (TimeoutException, NoSuchElementException):
            self._log_action("not_found", description)
        except Exception as e:
            self._log_action("error", description,e)

    # Input genérico (escribir texto en un campo)
    def input_element(self, locator, description="elemento", value="valor"):
        try:
            element = self.waits.wait_for_element(locator,description)
            element.clear()
            element.send_keys(value)

        except (TimeoutException, NoSuchElementException):
            self._log_action("not_found", description)
        except Exception as e:
            self._log_action("error", description,e)


    def _log_action(self, status: str, description: str, str = ""):
        if status == "ok":
            logger.info(f" Clic en  {description}")
        elif status == "not_found":
            logger.error(f"❌ No se encontró {description} en {self.timeout} segundos")
        else:
            logger.error(f"⚠ Error inesperado al intentar hacer clic en {description}: {str}")

    """Retorna True si el elemento es visible, False si no lo está."""
    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False