from e2e.pages.mobile.home_page import HomPage
from e2e.core.logger import logger
import time


def test_aceptar_terminos(driver):
    home = HomPage(driver)
    home.aceptar_terminos()
    home.aceptar_permisos_ubicacion()
    home.aceptar_permisos_llamada()

    logger.info("Validando que se abrió la pantalla de permisos...")
    assert home.esta_visible(), "La pantalla de permisos no se mostró como se esperaba"

    time.sleep(5)
