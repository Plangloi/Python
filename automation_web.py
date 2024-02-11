from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://crosemont.omnivox.ca/Login/Account/Login?erreur=&L=FRA&ReturnUrl=%2fintr")
    page.get_by_placeholder("0000000").click()
    page.get_by_placeholder("0000000").fill("6281807")
    page.get_by_placeholder("0000000").press("Tab")
    page.get_by_placeholder("••••••••").fill("lokozchicoutimi69")
    page.get_by_role("button", name="navigate_next Connexion").click()
    page.wait_for_load_state("networkidle")
    #page.get_by_role("link", name="Léa").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name="Relevé de notes finales").click()

    # ---------------------
    context.close()
# browser.close()


with sync_playwright() as playwright:
    run(playwright)

