from playwright.sync_api import sync_playwright, Page
import pytest
    
LOGIN_LINK = "https://www.avito.ru/avito-care/eco-impact"
BACKEND_LINK = "https://www.avito.ru/web/1/charity/ecoImpact/init"
METER_CO2 = "//img[contains(@class, 'xXtiX')]/.."
METER_WATER = "//img[contains(@class, 'LWlZZ')]/.."
METER_ENERGY = "//img[contains(@class, 'JCEQH')]/.."

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_zero_meter(page: Page):
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/zero_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/zero_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/zero_meter_energy.png")

def test_one_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_one.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/one_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/one_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/one_meter_energy.png")

def test_import_999_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_999.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_999_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_999_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_999_meter_energy.png")

def test_import_1000_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_1000.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_1000_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_1000_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_1000_meter_energy.png")

def test_import_1500_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_1500.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_1500_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_1500_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_1500_meter_energy.png")

def test_import_999999_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_999999.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_999999_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_999999_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_999999_meter_energy.png")

def test_import_1000000_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_1000000.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_1000000_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_1000000_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_1000000_meter_energy.png")

def test_import_9999999_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_9999999.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_9999999_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_9999999_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_9999999_meter_energy.png")

def test_import_1000000000_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_1000000000.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_1000000000_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_1000000000_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_1000000000_meter_energy.png")

def test_import_9999999999_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_9999999999.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_9999999999_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_9999999999_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_9999999999_meter_energy.png")

def test_import_1000000000000_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_1000000000000.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_1000000000000_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_1000000000000_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_1000000000000_meter_energy.png")

def test_import_9999999999999_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_import_9999999999999.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/import_9999999999999_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/import_9999999999999_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/import_9999999999999_meter_energy.png")

def test_abroad_max_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_abroad_max.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/abroad_max_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/abroad_max_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/abroad_max_meter_energy.png")

def test_negative_number_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_negative_number.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/negative_number_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/negative_number_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/negative_number_meter_energy.png")

@pytest.mark.xfail
def test_letter_meter(page: Page):
    page.route(BACKEND_LINK, lambda route: route.fulfill(path="auto_json/test_letter.json"))
    page.goto(LOGIN_LINK)
    meter_co2 = page.locator(METER_CO2)
    meter_co2.screenshot(path="output/letter_meter_co2.png")
    meter_water= page.locator(METER_WATER)
    meter_water.screenshot(path="output/letter_meter_water.png")
    meter_energy= page.locator(METER_ENERGY)
    meter_energy.screenshot(path="output/letter_meter_energy.png")

