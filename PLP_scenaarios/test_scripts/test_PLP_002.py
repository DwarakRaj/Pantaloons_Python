from PLP_scenaarios.pom_files.plp_001_pom import pm_cl_plp_001
from time import sleep
from pytest import mark

@mark.PLP_002
def test_TCPLP_009(_driver):
    r = pm_cl_plp_001(_driver)
    r.mouse_hov_men()
    r.click_Farmal_trousers()
    sleep(5)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_002_reports_jpeg\tcplp_009_1.jpeg")
    r.page_down()
    sleep(10)
    r.mouse_hover_item_Farmal_trousers()
    sleep(8)
    _driver.get_screenshot_as_file(r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\PLP_scenaarios\test_reports\PLP_002_reports_jpeg\tcplp_009_2.jpeg")
