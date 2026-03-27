import time
from appium.webdriver.common.appiumby import AppiumBy
from e2e.core.base_page import BasePage

class AssignedPage(BasePage):

    contenedor_assigned = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(14)'
    )

    def ir_mapa(self):
        self.click_element(
            self.contenedor_assigned,
            "contenedor_assistance_proces"
        )

    def content_card_visible(self):
        return self.is_visible(self.contenedor_assigned)