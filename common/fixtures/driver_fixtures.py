import pytest
from common.config.capabilities import get_android_options
from playwright.sync_api import sync_playwright
from e2e.core.logger import logger



"""
Se ejecuta una sola vez por corrida de pytest...
"""

@pytest.fixture(scope="session")
def driver_android():
    from e2e.utils.driver import get_driver

    logger.info(">>> Iniciando driver Android")

    options = get_android_options()
    driver = get_driver(options)

    yield driver

    logger.info(">>> Cerrando driver Android")
    if driver:
        try:
            driver.quit()
        except Exception:
            logger.exception("Error cerrando driver Android")


@pytest.fixture(scope="session")
def browser_playwright():
    logger.info(">>> Iniciando navegador Chromium con Playwright")

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser

    logger.info(">>> Cerrando navegador Chromium")

    if browser:
        try:
            browser.close()
        except Exception:
            logger.exception("Error cerrando browser")

    if playwright:
        try:
            playwright.stop()
        except Exception:
            logger.exception("Error cerrando playwright")
