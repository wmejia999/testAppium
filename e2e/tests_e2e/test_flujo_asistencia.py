from urllib3 import request

from pages.mobile.request_page import RequestsPage
from pages.mobile.login_page import LoginPage
from pages.mobile.assigned_page import AssignedPage
from pages.mobile.map_page import MapPage

#Parte 1: Aceptar servicio emergencia
def test_login_aceptar_asistencia(driver):
    try:
        login = LoginPage(driver)
        requests = RequestsPage(driver)

        # Paso 1: Login
        login.ingresar_credenciales("automatizacionika", "123")
        login.login()

        # Paso 2: Validar alerta de permisos
        if requests.btn_GPS_visible():
            requests.aceptar_permiso_GPS()

        # Paso 3: Aceptar y confirmar servicio
        requests.aceptar_asistencia()
        requests.confirmar_asistencia()

        assert requests.contenedor_visible()

    except Exception as e:
        print(f"Error durante la prueba: {e}")

#Parte 2: Iniciar servicio
def test_flujo_asistencia(driver):
    try:
        assigned = AssignedPage(driver)
        map = MapPage(driver)

        # Paso 1: Login
        assigned.ir_mapa()
        map.quemar_etapa("#Monitoreo")
        map.quemar_etapa("#Arribo")
        map.quemar_etapa("#Diagnostico")
        map.quemar_etapa("#Costeo")
        map.quemar_etapa("#Solución")

    except Exception as e:
        print(f"Error durante la prueba: {e}")