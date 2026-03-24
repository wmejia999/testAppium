from e2e.pages.mobile.home_page import HomPage
from e2e.pages.mobile.login_page import LoginPage


class MobileFlow:
    """Flujos de negocio para la parte mobile.

    Métodos públicos representan intenciones de negocio y combinan llamadas a
    Page Objects móviles.
    """

    def __init__(self, driver):
        self.home = HomPage(driver)
        self.login = LoginPage(driver)

    def login_y_aceptar_terminos(self, usuario: str, contrasena: str):
        """Realiza el flujo completo de aceptación de términos, permisos y login.

        Entrada: usuario, contrasena
        Salida: None (lanza excepción si falla)
        """
        # Aceptar terminos y permisos
        self.home.aceptar_terminos()
        self.home.aceptar_permisos_ubicacion()
        self.home.aceptar_permisos_llamada()

        # Login
        self.login.ingresar_credenciales(usuario, contrasena)
        self.login.login()
        if not self.login.alert_esta_visible():
            raise AssertionError("El login no mostró el alert esperado")
