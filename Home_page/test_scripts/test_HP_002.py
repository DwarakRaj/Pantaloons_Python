from Home_page.pom_class_files.hp_pom_001_002 import Pom_cl_hp_001_002
from pytest import mark
from time import sleep
@mark.tc2
def test_TCHP_002(_driver):
    po = Pom_cl_hp_001_002(_driver)
    sleep(5)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\Home_page\test_reports\HP_002\TCHP_002.jpeg")



