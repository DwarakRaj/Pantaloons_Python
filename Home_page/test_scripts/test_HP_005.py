from Home_page.pom_class_files.hp_pom_005 import Pom_cl_hp_005
from pytest import mark
from time import sleep
@mark.tc7
def test_TCHP_007(_driver):
    po = Pom_cl_hp_005(_driver)
    handles = _driver.window_handles
    po.mouse_hov_women()
    po.click_women_brand()
    sleep(12)
    po.screen_shot_capture(r"\HP_005\TCHP_007_women.jpeg")
    _driver.back()
    sleep(8)
    po.mouse_hov_men()
    po.click_men_brand()
    sleep(8)
    po.screen_shot_capture(r"\HP_005\TCHP_007_MEN.jpeg")
    _driver.back()
    sleep(8)
    po.mouse_hov_kids()
    po.click_kids_brand()
    sleep(8)
    po.screen_shot_capture(r"\HP_005\TCHP_007_kids.jpeg")
