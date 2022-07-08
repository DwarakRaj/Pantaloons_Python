from Home_page.pom_class_files.hp_pom_001_002 import Pom_cl_hp_001_002
from pytest import mark
from time import sleep
@mark.tc1
def test_TCHP_001(_driver):
    po = Pom_cl_hp_001_002(_driver)
    sleep(5)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\Home_page\test_reports\HP_001\TCHP_001.jpeg")

