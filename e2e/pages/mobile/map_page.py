import time
from appium.webdriver.common.appiumby import AppiumBy
from e2e.core.base_page import BasePage

class MapPage(BasePage):

    contenedor_mapa = (AppiumBy.ACCESSIBILITY_ID, "Mapa de Google")

    def quemar_etapa(self, stage):
        self.click_element(
            (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("' + stage + '")'),
            "btn_manage_stage" + stage
        )

    def boton_etapa_visible(self, stage):
        return self.is_visible((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("' + stage + '")'))

    def content_card_mapa_visible(self):
        return self.is_visible(self.contenedor_mapa)
