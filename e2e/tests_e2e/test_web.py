import pytest
from e2e.pages.mobile.home_page import HomPage
from e2e.pages.mobile.login_page import LoginPage
from e2e.tests_e2e.web.tests.example_web import test_login_y_creacion_expediente_web

@pytest.mark.e2e
def test_flujo_login_y_aceptacion_terminos(driver):
    try:
        home = HomPage(driver)
        login = LoginPage(driver)

        # Paso 1: aceptar terminos y permisos
        home.aceptar_terminos()

        # Paso 2: aceptar permisos
        home.aceptar_permisos_ubicacion()
        home.aceptar_permisos_llamada()

        # Paso 3: Login
        login.ingresar_credenciales("preikaw", "123")
        login.login()
        assert login.alert_esta_visible()

    except Exception as e:
        print(f"Error durante la prueba: {e}")

# ====== TEST WEB (Playwright Python) ======
@pytest.mark.e2e
def test_web_login_y_flujo():
    print("=== TEST WEB (Playwright Python) ===")
    test_login_y_creacion_expediente_web()

