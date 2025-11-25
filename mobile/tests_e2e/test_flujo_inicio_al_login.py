from mobile.pages.home_page import HomPage
from mobile.pages.login_page import LoginPage

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
        login.ingresar_credenciales("ika.17", "1234")
        login.login()
        assert login.alert_esta_visible()

    except Exception as e:
        print(f"Error durante la prueba: {e}")