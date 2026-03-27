from typing import Tuple, Any
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from e2e.core.logger import logger
from e2e.core.waits import Waits

"""
Centraliza las acciones sobre los elementos.
Todas las clases heredarán esta clase.
"""

class BasePage:

    def __init__(self, driver, timeout=3000):
        self.driver = driver
        self.timeout = timeout
        self.waits = Waits(driver, timeout)

    # Click genérico
    def click_element(self, locator, description="elemento"):
        try:
            element = self.waits.wait_for_element(locator, description)
            element.click()
            self._log_action("ok", description)

        except (TimeoutException, NoSuchElementException) as e:
            logger.exception(f"No se encontró/esperó el elemento '{description}'")
            self._log_action("not_found", description, str(e))
            raise
        except Exception as e:
            logger.exception(f"Error inesperado al intentar hacer clic en {description}")
            self._log_action("error", description, str(e))
            raise

    # Input genérico (escribir texto en un campo)
    def input_element(self, locator, description="elemento", value="valor"):
        try:
            element = self.waits.wait_for_element(locator, description)
            element.clear()
            element.send_keys(value)

        except (TimeoutException, NoSuchElementException) as e:
            logger.exception(f"No se encontró/esperó el elemento '{description}' para ingresar texto")
            self._log_action("not_found", description, str(e))
            raise
        except Exception as e:
            logger.exception(f"Error inesperado al intentar escribir en {description}")
            self._log_action("error", description, str(e))
            raise

    def _log_action(self, status: str, description: str, error: str = ""):
        if status == "ok":
            logger.info(f"Clic en {description}")
        elif status == "not_found":
            logger.error(f"❌ No se encontró {description} en {self.timeout} segundos. Detalle: {error}")
        else:
            logger.error(f"⚠ Error inesperado al intentar {description}: {error}")

    #Retorna True si el elemento es visible, False si no lo está.
    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            # No es una situación excepcional para fallar la prueba; devolvemos False
            logger.debug(f"Elemento {locator} no visible en 5s")
            return False
        except Exception as e:
            # Cualquier otro error se registra y se devuelve False para que la
            # lógica del test decida si fallar o no en base al assert correspondiente.
            logger.exception("Error verificando visibilidad del elemento")
            return False

