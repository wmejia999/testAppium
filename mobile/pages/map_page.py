import time
from appium.webdriver.common.appiumby import AppiumBy
from mobile.core.base_page import BasePage

class MapPage(BasePage):

    btn_manage_stage = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(6)'
    )

    def quemar_etapa(self, stage):
        self.click_element(
            self.btn_manage_stage,
            "btn_manage_stage" + stage
        )

    def content_card_visible(self):
        return self.btn_manage_stage
