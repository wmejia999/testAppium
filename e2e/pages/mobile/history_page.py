from appium.webdriver.common.appiumby import AppiumBy
from e2e.core.base_page import BasePage
from e2e.core.waits import Waits

class HistoyPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.wait = Waits(driver, timeout)

    def ver_detalle_historico(self):
        self.click_element(
            (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Historial")'),
            "ir a historico"
        )
        self.click_element(
            (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(4)'),
            "ver historico"
        )

        self.wait.wait_for_element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tuapp:id/detailContainer")'),
            "Pantalla de detalle"
        )

        self.click_element(
            (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(5)'),
            "ir atras"
        )

    def esta_visible(self):
        return self.is_visible((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(4)'))