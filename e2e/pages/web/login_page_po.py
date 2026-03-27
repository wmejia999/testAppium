from playwright.sync_api import Page


class LoginPage:
    """Page Object para la página de login y acciones relacionadas con expedientes.

    API pública (ejemplos):
    - goto()
    - login(username, password)
    - select_platform(name)
    - go_to_expedientes()
    - open_seleccion_afiliado()
    - fill_datos_afiliado(datos)
    - confirm_seleccion()
    - copy_info_afiliado()
    """

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://soa.sistemaoperaciones.com/soa/auth/login"

        # Selectors
        self._input_user = "input[name='username']"
        self._input_pwd = "input[name='password']"
        self._btn_login = "#kt_sign_in_submit"
        self._platform_selector = "#plataform"
        self._expedientes_btn = "b:has-text('Expedientes')"

    def goto(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.fill(self._input_user, username)
        self.page.fill(self._input_pwd, password)
        self.page.click(self._btn_login)

    def select_platform(self, name: str = "Ikatech"):
        # Click en el selector y elegir la opción por texto
        self.page.locator(self._platform_selector).click()
        # Uso de get_by_role para seleccionar por nombre (Playwright)
        self.page.get_by_role("option", name=name).click()

    def go_to_expedientes(self):
        self.page.click(self._expedientes_btn)

    # --- Expediente related actions ---
    def open_seleccion_afiliado(self):
        self.page.get_by_role("button", name="Selección del afiliado").click()

    def fill_datos_afiliado(self, datos: str):
        self.page.get_by_role("textbox", name="Datos").fill(datos)

    def confirm_seleccion(self):
        self.page.get_by_role("button", name="Seleccionar").click()

    def copy_info_afiliado(self):
        self.page.get_by_role("button", name="Copiar info Afiliado").click()
