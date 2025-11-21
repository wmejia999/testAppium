import pytest
from mobile.utils.driver import get_driver
"""
scope="session" define que la misma instancia de driver se usará para todos los tests de la sesión.
yield entrega el driver a cada prueba que lo necesite.
"""

@pytest.fixture(scope="session")
def driver():
    print(">>> Iniciando driver de Appium")
    driver = get_driver()
    yield driver
    print(">>> Cerrando driver de Appium")
    driver.quit()
