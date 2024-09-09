from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.com/")
    page.get_by_placeholder("Search Amazon").click()
    page.get_by_placeholder("Search Amazon").fill("iphone 15")
    page.get_by_role("button", name="iphone 15", exact=True).click()
    expect(page.locator("heading"))
    page.get_by_role("heading", name="Apple iPhone 15 Pro Max, 1TB, Natural Titanium - GSM Carriers (Renewed)").get_by_role("link", name="Apple iPhone 15 Pro Max, 1TB, Natural Titanium - GSM Carriers (Renewed)").click()
    page.get_by_role("button", name="256GB").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
