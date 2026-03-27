from appium.webdriver.webdriver import WebDriver

from e2e.conftest import driver
from e2e.pages.mobile.assigned_page import AssignedPage
from e2e.pages.mobile.home_page import HomPage
from e2e.pages.mobile.login_page import LoginPage
from e2e.pages.mobile.map_page import MapPage
from e2e.pages.mobile.request_page import RequestsPage


class MobileFlow:
    """Flujos de negocio para la parte mobile.

    Métodos públicos representan intenciones de negocio y combinan llamadas a
    Page Objects móviles.
    """

    def __init__(self, driver):
        self.home = HomPage(driver)
        self.login = LoginPage(driver)
        self.assigned = AssignedPage(driver)
        self.map_app = MapPage(driver)
        self.requests = RequestsPage(driver)

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

    def login_exitoso_visible(self):
        """Devuelve si el toast de login exitoso está visible."""
        return self.login.contenedor_alert_duplicidad_visible()

    def aceptar_servicio(self):
        """acepta el servicio desde la app móvil."""

        # Paso 3: Aceptar y confirmar servicio
        self.requests.aceptar_asistencia()
        self.requests.confirmar_asistencia()

    def contenedor_car_ir_a_mapa_visible(self):
        """Devuelve si el contenedor para ir al mapa está visible."""
        return self.assigned.content_card_visible()

    def ir_a_mapa(self):
        """Navega a la pantalla del mapa desde la vista de asistencia asignada."""
        self.assigned.ir_mapa()

    def contenedor_mapa_visible(self):
        """Devuelve si el contenedor del mapa está visible."""
        return self.map_app.content_card_mapa_visible()

    def boton_etapa_visible(self, etapa: str):
        """Devuelve si el botón para quemar la etapa está visible."""
        return self.map_app.boton_etapa_visible(etapa)

    def gestion_etapas_servicio(self):
        """ Gestiona las etapas del servicio desde la app móvil."""
        self.map_app.quemar_etapa("Realizar Monitoreo")
        self.map_app.quemar_etapa("Confirmar arribo")
        self.map_app.quemar_etapa("Realizar Diagnóstico")
        self.map_app.quemar_etapa("Realizar Costos")
        self.map_app.quemar_etapa("Realizar Solución")


