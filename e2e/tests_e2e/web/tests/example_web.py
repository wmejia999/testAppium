# example_web.py
from playwright.sync_api import Page, expect

def test_login_y_creacion_expediente_web(page):
   """
  print("=== TEST WEB (Playwright Python) ===")
    page.goto("https://soa.sistemaoperaciones.com/soa/auth/login")

    page.fill("input[name='username']", "IKATECHPRUEBAS")
    page.fill("input[name='password']", "App123456*")
    page.click("#kt_sign_in_submit")

    page.locator("#plataform").click()
    page.get_by_role("option", name="Ikatech").click()

    page.click("b:has-text('Expedientes')")

    # Creación de expediente
    page.get_by_role("button", name="Selección del afiliado").click()
    page.get_by_role("textbox", name="Datos").fill("00001-123-321")
    page.get_by_role("button", name="Seleccionar").click()
    page.get_by_role("button", name="Copiar info Afiliado").click()"""

