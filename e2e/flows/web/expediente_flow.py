from e2e.pages.web.login_page_po import LoginPage as LoginWebPage
from e2e.pages.web.expediente_page import ExpedientePage


class WebFlow:
    """Flujos de negocio para la parte web.

    Encapsula acciones de alto nivel como crear un expediente para un afiliado
    y verificar que el expediente se haya creado.
    """

    def __init__(self, page):
        self.login = LoginWebPage(page)
        self.expediente = ExpedientePage(page)
        self.page = page

    def login_y_seleccionar_plataforma(self, usuario: str, contrasena: str, plataforma: str = "Ikatech"):
        self.login.goto()
        self.login.login(usuario, contrasena)
        self.login.select_platform(plataforma)
        self.login.go_to_expedientes()

    def crear_expediente_para(self, datos_afiliado: str, telefono: str, lat: str, lon: str, direccion_fragment: str):
        """Crea un expediente para el afiliado identificado por `datos_afiliado`.

        Este método agrupa todos los pasos técnicos necesarios y deja el test
        a nivel de intención de negocio.
        """
        self.expediente.go_to_monitor()
        self.expediente.click_nuevo()
        self.expediente.open_seleccion_afiliado()
        self.expediente.search_afiliado(datos_afiliado)
        self.expediente.confirm_seleccion()
        self.expediente.copy_info_afiliado()
        self.expediente.fill_phones(telefono)
        self.expediente.add_nueva_ubicacion()
        self.expediente.select_departamento()
        self.expediente.select_municipio()
        self.expediente.select_localidad()
        self.expediente.fill_lat_long(lat, lon)
        self.expediente.buscar_direccion()
        self.expediente.select_address_from_results(direccion_fragment)
        self.expediente.guardar_ubicacion()
        self.expediente.crear_expediente()

    def verificar_expediente_creado(self ):
        from playwright.sync_api import expect

        # Ubicar el bloque que contiene el texto fijo
        bloque = self.page.locator("div.border").filter(has_text="Expediente").first

        # Dentro de ese bloque buscar el número
        numero_locator = bloque.locator("div.fw-bold.fs-6.text-gray-400")

        expect(numero_locator).to_be_visible(timeout=10000)

        numero = numero_locator.inner_text().strip()

        # Validaciones correctas
        assert numero is not None
        assert numero.isdigit()
