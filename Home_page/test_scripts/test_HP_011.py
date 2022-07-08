from Home_page.pom_class_files.hp_pom_008 import Pom_cl_hp_008
from pytest import mark
from time import sleep

@mark.tc15
def test_TCHP_015(_driver):
    po = Pom_cl_hp_008(_driver)
    sleep(10)
    po.page_down()
    po.mouse_hover_hp_product()
    po.screen_shot_capture(r"\HP_011\TCHP15_before_click_logo.jpeg")
    sleep(8)
    po.click_hp_product()
    sleep(8)
    po.screen_shot_capture(r"\HP_011\TCHP15_after_click_logo.jpeg")
    po.click_pantaloons_logo()
    sleep(8)
    po.screen_shot_capture(r"\HP_011\TCHP15_back_to_hp.jpeg")