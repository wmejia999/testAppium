import allure
import pytest

from e2e.flows.mobile.mobile_login_permisos_flow import MobileFlow
from e2e.flows.web.expediente_flow import ExpedientFlow

@allure.feature() #
@pytest.mark.e2e
def test_flujo_login_y_aceptacion_terminos(driver):
    # Historia de negocio: autenticar en la app móvil y aceptar términos y permisos
    mobile_flow = MobileFlow(driver)
    mobile_flow.login_y_aceptar_terminos("automobile1", "App123456*")
    assert mobile_flow.login_exitoso_visible(), "contenedor de sesión duplicada no visible después de login"


@allure.feature()
@pytest.mark.e2e
def test_login_soa_crea_expediente_y_asistencia(page):
    # Historia de negocio: autenticar en web, crear expediente para un afiliado y verificarlo
    web_flow = ExpedientFlow(page)
    web_flow.login_y_seleccionar_plataforma("IKATECHPRUEBAS", "App123456*", "Ikatech")
    web_flow.crear_expediente_para(
        datos_afiliado="WEN24",
        telefono="1234567890",
        lat="4.8056605129510634",
        lon="-75.68292189119606",
        direccion_fragment="Cra. 15 #4-42, Pereira",
    )

    numero_expediente = web_flow.verificar_expediente_creado()
    assert numero_expediente is not None, "Expediente no creado o número no encontrado"

    web_flow.crear_asistencia_enviar_solicitud()
    page.close()

@allure.feature()
@pytest.mark.e2e
def test_aceptar_servicio_app(driver):
    # Historia de negocio: aceptar servicio desde la app móvil y gestionar las etapas del servicio
    mobile_flow2 = MobileFlow(driver)
    mobile_flow2.aceptar_servicio()
    assert mobile_flow2.contenedor_car_ir_a_mapa_visible(),\
        "El contenedor para ir al mapa no se mostró después de aceptar el servicio"
    mobile_flow2.ir_a_mapa()
    assert mobile_flow2.contenedor_mapa_visible(), \
        "El contenedor del mapa no se mostró después de navegar al mapa"
    mobile_flow2.gestion_etapas_servicio()
