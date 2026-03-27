from playwright.sync_api import Page
import re

"""Page Object para acciones relacionadas con la creación de expedientes y la
    sección "Monitor de Novedades".

    Provee métodos de alto nivel que encapsulan los selectores y las acciones
    originales del test plano.
    """
class ExpedientePage:

    def __init__(self, page: Page):
        self.page = page

    def get_id_expediente(self):
        expediente_block = self.page.get_by_text("Expediente").locator("xpath=..")
        expediente_num = expediente_block.locator("xpath=./following-sibling::div[contains(@class,'fw-bold')]")
        return expediente_num

    def go_to_monitor(self):
        # Link exacto al "Monitor de Novedades"
        self.page.get_by_role("link", name=" Monitor de Novedades", exact=True).click()

    def click_nuevo(self):
        self.page.get_by_role("button", name=" Nuevo").click()

    def open_seleccion_afiliado(self):
        self.page.get_by_role("button", name="Selección del afiliado").click()

    def search_afiliado(self, datos: str):
        # Rellena el textbox y pulsa el botón de búsqueda (lupa)
        self.page.get_by_role("textbox", name="Datos").fill(datos)
        self.page.get_by_role('button', name="").click()

    def confirm_seleccion(self):
        self.page.get_by_role("button", name="Seleccionar").click()

    def copy_info_afiliado(self):
        self.page.get_by_role("button", name="Copiar info Afiliado").click()

    def fill_phones(self, phone: str):
        self.page.get_by_role("textbox", name="Phones").click()
        self.page.get_by_role("textbox", name="Phones").fill(phone)

    def add_nueva_ubicacion(self):
        # Abrir modal/menú de ubicaciones
        self.page.get_by_role("button", name="").click()
        self.page.get_by_role("button", name="Nueva Ubicación").click()

    def select_departamento(self, name: str = "DISTRITO NACIONAL"):
        # Selector por CSS y luego opción por texto
        self.page.locator(".d-flex > .form-control").first.click()
        self.page.get_by_role("option", name=name).click()

    def select_municipio(self, name: str = "SANTO DOMINGO DE GUZMÁN"):
        # Selector más específico que usa un filtro por texto
        self.page.locator("div").filter(has_text=re.compile(r"^Selecciona una opción$")).nth(3).click()
        self.page.get_by_role("option", name=name).click()

    def select_localidad(self, name: str = "SANTO DOMINGO DE GUZMÁN"):
        self.page.locator("div:nth-child(3) > .d-flex > .form-control > .css-13cymwt-control").click()
        self.page.get_by_role("option", name=name).click()

    def fill_lat_long(self, lat: str, lon: str):
        self.page.get_by_role("textbox", name="Latitud").click()
        self.page.get_by_role("textbox", name="Latitud").fill(lat)
        # Asegurarse de enfocar Longitud antes de rellenar
        self.page.locator("div").filter(has_text=re.compile(r"^Longitud$")).click()
        self.page.get_by_role("textbox", name="Longitud").click()
        self.page.get_by_role("textbox", name="Longitud").fill(lon)

    def buscar_direccion(self):
        self.page.get_by_role("button", name="Buscar").click()

    def select_address_from_results(self, text_fragment: str):
        # Selecciona el resultado que contenga el texto proporcionado
        self.page.locator("a").filter(has_text=text_fragment).click()

    def guardar_ubicacion(self):
        self.page.get_by_role("button", name="Guardar ").click()

    def crear_expediente(self):
        self.page.get_by_role("button", name="Crear expediente ").click()

    def crear_asistance(self):
        self.page.get_by_role("button", name=" Nuevo").click()
        self.page.locator("div").filter(has_text=re.compile(r"^CERRAJERIA$")).nth(1).click()
        self.page.locator("div").filter(has_text=re.compile(r"^Automatización móvil \(NO TOCAR\)Disponibles: IlimitadoDetalle$")).nth(4).click()
        self.page.get_by_title("Copiar dirección del").click()
        self.page.locator(
            ".row > div:nth-child(2) > .form-control > .css-13cymwt-control > .css-1wy0on6 > .css-1xc3v61-indicatorContainer").click()
        self.page.get_by_role("option", name="Casa").click()

        self.page.locator(
            "div:nth-child(3) > .form-control > .css-13cymwt-control > .css-1wy0on6 > .css-1xc3v61-indicatorContainer > .css-8mmkcg").click()
        self.page.get_by_role("option", name="EMERGENCIA").click()
        self.page.get_by_role("button", name="Guardar").click()
        self.page.get_by_role("button", name="Solicitud app proveedores").click()
        self.page.wait_for_timeout(5000)  # Esperar 5s para que se procese la creación






