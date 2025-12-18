import time
from appium.webdriver.common.appiumby import AppiumBy
from mobile.core.base_page import BasePage

class RequestsPage(BasePage):

    contenedor_assigned = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(9)'
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
        self.click_element(
            self.check_activar_ubicacion,
            "check_activar_ubicacion"
        )


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

    #Esta alerta se genera cuando se detecta que no hay permisos de GPS
    def btn_GPS_visible(self):
        return self.is_visible(self.btn_encender_GPS)

    def contenedor_visible(self):
        return self.is_visible(self.contenedor_assigned)


    def content_card_visible(self):
        return self.is_visible(self.content_card_asistances)