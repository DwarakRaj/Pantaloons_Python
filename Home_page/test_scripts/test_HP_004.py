from Home_page.pom_class_files.hp_pom_004 import Pom_cl_hp_004
from pytest import mark
from time import sleep
@mark.tc6
def test_TCHP_006(_driver):
    po = Pom_cl_hp_004(_driver)
    po.mouse_hov_women()
    po.shop_by_occation_women()
    sleep(12)
    po.screen_shot_capture(r"\HP_004\TCHP_006_women.jpeg")
    po.mouse_hov_men()
    po.shop_by_occation_men()
    sleep(8)
    po.screen_shot_capture(r"\HP_004\TCHP_006_MEN.jpeg")
    po.mouse_hov_kids()
    po.shop_by_occation_kids()
    sleep(8)
    po.screen_shot_capture(r"\HP_004\TCHP_006_kids.jpeg")
