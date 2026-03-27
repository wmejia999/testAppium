from e2e.core.logger import logger
import pytest
from e2e.pages.mobile.login_page import LoginPage

def test_login_empty(driver):
    logger.info("Iniciando test_login_empty")
    login = LoginPage(driver)
    login.ingresar_credenciales("","")
    login.login()
    assert login.text_esta_visible()

def test_password_incorrecto(driver):
    logger.info("Iniciando test_password_incorrecto")
    login = LoginPage(driver)
    login.ingresar_credenciales("ika","0000")
    login.login()
    assert login.toast_esta_visible()

def test_login_correcto(driver):
    logger.info("Iniciando test_login_correcto")
    login = LoginPage(driver)
    login.ingresar_credenciales("preikaw","123")
    login.login()
    assert login.alert_esta_visible()
