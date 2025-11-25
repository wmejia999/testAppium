import time
from appium.webdriver.common.appiumby import AppiumBy
from mobile.core.base_page import BasePage

class LoginPage(BasePage):

    contenedor = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(2)'
    )

    btn_encender_GPS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)'
    )

    check_activar_ubicacion = (
        AppiumBy.ID,
        'com.android.settings:id/switch_widget'
    )

    toast_empty_asistances = (
        AppiumBy.XPATH,
        '//android.widget.Toast[@text="No hay asistencias disponibles en el momento."]'
    )

    content_card_asistances = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(3)'
    )

    card_asistances = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(4)'
    )

    btn_accept_asistances = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)'
    )

    btn_confirm_asistances = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)'
    )

    def aceptar_permiso_GPS(self):
        self.click_element(
            self.btn_encender_GPS,
            "btn_encender_GPS"
        )
        self.driver.back()
        self.driver.back()


    def ver_detalle_asistencia(self):
        self.click_element(
            self.card_asistances,
            "card_asistances"
        )
        self.driver.back()

    def aceptar_asistencia(self):
        self.click_element(
            self.btn_accept_asistances,
            "btn_accept_asistances"
        )

    def confirmar_asistencia(self):
        self.click_element(
            self.btn_confirm_asistances,
            "btn_confirm_asistances"
        )


    def contenedor_visible(self):
        return self.is_visible(self.contenedor)

    def toast_visible(self):
        return self.is_visible(self.toast_empty_asistances)

    def content_card_visible(self):
        return self.is_visible(self.content_card_asistances)