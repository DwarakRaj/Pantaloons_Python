from Home_page.pom_class_files.hp_pom_008 import Pom_cl_hp_008
from pytest import mark
from time import sleep

@mark.tc15
def test_TCHP_016(_driver):
    po = Pom_cl_hp_008(_driver)
    po.page_down()
    po.mouse_hover_show_recomonds()
    sleep(15)
    po.screen_shot_capture(r"\HP012\TCHP.jpeg")