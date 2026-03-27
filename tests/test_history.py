from e2e.pages.mobile.history_page import HistoryPage
from e2e.core.logger import logger


def test_history_visible(driver):
    history = HistoryPage(driver)
    history.open()
    logger.info("Validando que se abrió la pantalla de historial...")
    assert history.is_visible(), "La pantalla de historial no se mostró como se esperaba"
