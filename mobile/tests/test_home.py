from mobile.pages.home_page import HomPage
import time

def test_aceptar_terminos(driver):

    try:
        home = HomPage(driver)
        home.aceptar_terminos()
        home.aceptar_permisos_ubicacion()
        home.aceptar_permisos_llamada()

        print("Validando que se abrió la pantalla de permisos...")
        assert home.esta_visible()

        time.sleep(5)

    except Exception as e:
        print(f"Error durante la prueba: {e}")
        #explicacion = analizar_error_con_ia(str(e))
        #print(f"🔍 Análisis IA:\n{explicacion}")
        raise  # para que pytest marque el test como fallido