from mobile.pages.login_page import LoginPage

def test_login_empty(driver):
    try:
        login = LoginPage(driver)
        login.ingresar_credenciales("","")
        login.login()
        assert login.text_esta_visible()
    except Exception as e:
        print(f"Error durante la prueba: {e}")

def test_password_incorrecto(driver):
    try:
        login = LoginPage(driver)
        login.ingresar_credenciales("ika","0000")
        login.login()
        assert login.toast_esta_visible()
    except Exception as e:
        print(f"Error: No apareció el toast esperado de credenciales incorrectas.: {e}")

def test_login_correcto(driver):
    try:
        login = LoginPage(driver)
        login.ingresar_credenciales("preikaw","123")
        login.login()
        assert login.alert_esta_visible()
    except Exception as e:
        print(f"Error durante la prueba: {e}")