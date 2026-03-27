from playwright.sync_api import sync_playwright


def launch_browser(headless: bool = True, browser_name: str = "chromium"):
    p = sync_playwright().start()
    browser = None
    if browser_name == "chromium":
        browser = p.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = p.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = p.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unknown browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()

    # devolvemos browser, context y page para que el caller cierre
    return p, browser, context, page
