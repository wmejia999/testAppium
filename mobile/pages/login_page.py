import time
from appium.webdriver.common.appiumby import AppiumBy
from mobile.core.base_page import BasePage

class LoginPage(BasePage):

    contenedor = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.FrameLayout").instance(0)'
    )
    input_user = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)'
    )
    input_password = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)'
    )
    btn_login = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)'
    )
    btn_ok_duplicidad = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.view.View").instance(3)'
    )
    toast_locator = (
        AppiumBy.XPATH,
        "//android.widget.Toast[@text='No se encontró una cuenta activa con las credenciales proporcionadas']"
    )
    text_empty = (
        AppiumBy.XPATH,
        "//android.widget.Toast[@text='No se encontró una cuenta activa con las credenciales proporcionadas']"
    )

    def ingresar_credenciales(self, usuario, contrasena):
        self.input_element(
            self.input_user,
            "campo_user",
            usuario
        )
        self.input_element(
            self.input_password,
            "campo_pass",
            contrasena
        )

    def login(self):
        time.sleep(5)
        self.click_element(
            self.btn_login,
            "boton_login"
        )

        self.click_element(
            self.btn_ok_duplicidad,
            "presionar_ok"
        )
        time.sleep(5)

    def toast_esta_visible(self):
        return self.is_visible(self.toast_locator)

    def text_esta_visible(self):
        return self.is_visible(self.text_empty)