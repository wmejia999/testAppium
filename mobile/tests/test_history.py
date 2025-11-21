from mobile.pages.history_page import HistoyPage

import time

def test_aceptar_terminos(driver):

    try:
        history = HistoyPage(driver)
        history.ver_detalle_historico()

        print("Validando que se abrió la pantalla de permisos...")
        assert history.esta_visible()

        time.sleep(10)

    except Exception as e:
        print(f"Error durante la prueba: {e}")
        #explicacion = analizar_error_con_ia(str(e))
        #print(f"🔍 Análisis IA:\n{explicacion}")
        raise  # para que pytest marque el test como fallido
