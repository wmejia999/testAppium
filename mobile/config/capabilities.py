from appium.options.android import UiAutomator2Options

def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "12"
    options.device_name = "RF8N11VLJLX"
    options.app_package = "com.addiuva.proveedor.soav2" # Usar app instalada
    options.app_wait_activity = "*"
    options.auto_grant_permissions = True
    options.no_reset = True
    return options

    #Usar app en formato APK
    #options.app = "/Users/wendymejia/Downloads/Apks/app-basenewsoa-qa.apk