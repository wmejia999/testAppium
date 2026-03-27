"""
Driver de sesión para Appium y Playwright.
scope='session': misma instancia compartida entre todos los tests.
yield entrega el driver/browser a cada prueba que lo declare como parámetro.
"""

from e2e.core.logger import logger
import pytest
from playwright.sync_api import sync_playwright
from e2e.utils.driver import get_driver
import allure


# Fixture para Appium
@pytest.fixture(scope="session")
def driver():
    logger.info('>>> Iniciando driver de Appium')
    driver = get_driver()
    yield driver
    logger.info('>>> Cerrando driver de Appium')
    try:
        driver.quit()
    except Exception:
        logger.exception('Error cerrando driver de Appium')


# Fixture para Playwright (Chromium visible)
@pytest.fixture(scope="session")
def browser():
    logger.info('>>> Iniciando navegador Chromium con Playwright')
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)

    yield browser

    logger.info('>>> Cerrando navegador Chromium')
    try:
        browser.close()
        playwright.stop()
    except Exception:
        logger.exception('Error cerrando navegador Chromium')


@pytest.fixture
def page(browser,request):
    context = browser.new_context()
    page = context.new_page()
    yield page
    #si el test ha fallado, adjunta un screenshot al reporte de Allure
    if getattr(getattr(request.node, "rep_call", None), "failed", False):
        allure.attach(page.screenshot(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
    context.close()


#
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
