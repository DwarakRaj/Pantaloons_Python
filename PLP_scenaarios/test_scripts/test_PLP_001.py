from PLP_scenaarios.pom_files.plp_001_pom import pm_cl_plp_001
from time import sleep
from pytest import mark
@mark.PLP_001
def test_TCPLP_001(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_women()
    r.click_suit_blazer_item()
    sleep(8)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_001.jpeg")

@mark.PLP_001
def test_TCPLP_002(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_women()
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_002.jpeg")
    r.click_suit_blazer_item()
    sleep(8)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_002_2.jpeg")

@mark.PLP_001
def test_TCPLP_003(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_men()
    r.click_Jeans_link()
    sleep(8)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_003.jpeg")


@mark.PLP_001
def test_TCPLP_004(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_kids()
    r.click_shirts_link()
    sleep(8)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_004.jpeg")

@mark.PLP_001
def test_TCPLP_005(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_home_decor()
    r.click_table_acces_link()
    sleep(8)
    r.page_down()
    sleep(5)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_005.jpeg")

@mark.PLP_001
def test_TCPLP_006(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hover_accessories()
    r.click_women_shoes_link()
    sleep(8)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_001_reports_jpeg\tcplp_006.jpeg")


@mark.PLP_001
def test_TCPLP_007(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_home_decor()
    r.click_table_acces_link()
    count_tuple = r.count_products_bottles()
    print(count_tuple)
    assert count_tuple[0] == count_tuple[1]

@mark.PLP_001
def test_TCPLP_008(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_home_decor()
    r.click_table_acces_link()
    count_tuple = r.count_products_coaster()
    print(count_tuple)
    assert count_tuple[0] == count_tuple[1]



