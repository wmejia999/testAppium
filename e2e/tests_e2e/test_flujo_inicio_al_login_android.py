from e2e.core.logger import logger
from e2e.pages.mobile.home_page import HomPage
from e2e.pages.mobile.login_page import LoginPage

def test_flujo_login_y_aceptacion_terminos(driver):
    logger.info("Iniciando flujo: inicio a login")

    home = HomPage(driver)
    login = LoginPage(driver)

    # Paso 1: aceptar terminos y permisos
    home.aceptar_terminos()

    # Paso 2: aceptar permisos
    home.aceptar_permisos_ubicacion()
    home.aceptar_permisos_llamada()

    # Paso 3: Login
    login.ingresar_credenciales("ika.17", "1234")
    login.login()

    assert login.contenedor_alert_duplicidad_visible(),"contenedor de sesión duplicada no visible después de login"
