from appium.webdriver.common.appiumby import AppiumBy
from e2e.core.base_page import BasePage
from e2e.core.logger import logger

class HomPage(BasePage):

    contenedor = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.FrameLayout").instance(0)'
    )
    btnAceptar = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Aceptar")'
    )
    btnPermitirUbicacion = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_foreground_only_button")'
    )
    btnPermitirSiempre = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.android.permissioncontroller:id/allow_always_radio_button")'
    )
    btnPermitirLlamada = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_button")'
    )

    def aceptar_terminos(self):
        logger.info("Aceptando terminos...")
        self.click_element(
            self.btnAceptar,
            "botón Aceptar"
        )

    def aceptar_permisos_ubicacion(self):
        logger.info("Aceptando Permisos de ubicación...")
        self.click_element(
            self.btnPermitirUbicacion,
            "Permitir ubicación mientras se usa la app"
        )
        self.click_element(
            self.btnPermitirSiempre,
            "Permitir siempre"
        )
        self.driver.back()

    def aceptar_permisos_llamada(self):
        logger.info("Aceptando Permisos de llamada...")
        self.click_element(
            self.btnPermitirLlamada,
            "Permitir llamadas siempre")

    def esta_visible(self):
        return self.is_visible(self.contenedor)