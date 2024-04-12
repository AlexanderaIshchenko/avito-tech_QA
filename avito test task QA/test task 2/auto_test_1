import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.avito.ru/avito-care/eco-impact"

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    yield browser
    print("\nquit browser")
    browser.quit()

class TestZeroMeter:

    def test_screen_meter_co_2(self, browser):
        first_meter = browser.find_element(By.XPATH, "//img[contains(@class, 'xXtiX')]/..")
        first_meter.screenshot(f".\\output\\zero_meter_co_2.png")

    def test_screen_meter_water(self, browser):
        second_meter = browser.find_element(By.XPATH, "//img[contains(@class, 'LWlZZ')]/..")
        second_meter.screenshot(f".\\output\\zero_meter_water.png")

    def test_screen_meter_watt(self, browser):
        third_meter = browser.find_element(By.XPATH, "//img[contains(@class, 'JCEQH')]/..")
        third_meter.screenshot(f".\\output\\zero_meter_watt.png")
