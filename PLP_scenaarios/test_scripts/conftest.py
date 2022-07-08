from selenium import webdriver
from pytest import fixture
@fixture
def _driver():
    driver = webdriver.Chrome(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\drivers\chromedriver.exe")
    driver.get("https://test.pantaloons.com")
    driver.maximize_window()
    yield driver
    driver.quit()
