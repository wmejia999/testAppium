import time
from appium.webdriver.common.appiumby import AppiumBy
from mobile.core.base_page import BasePage

class AssignedPage(BasePage):

    contenedor_assigned = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(9)'
    )

    def ir_mapa(self):
        self.click_element(
            self.contenedor_assigned,
            "btn_accept_asistances"
        )

    def content_card_visible(self):
        return self.is_visible(self.contenedor_assigned)