from e2e.pages.web.login_page_po import LoginPage


def test_login_y_creacion_expediente_web(page):
    lp = LoginPage(page)
    lp.goto()

    lp.login("IKATECHPRUEBAS", "App123456*")
    lp.select_platform("Ikatech")
    lp.go_to_expedientes()

    # Creación de expediente
    lp.open_seleccion_afiliado()
    lp.fill_datos_afiliado("00001-123-321")
    lp.confirm_seleccion()
    lp.copy_info_afiliado()
