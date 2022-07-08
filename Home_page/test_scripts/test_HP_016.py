from Home_page.pom_class_files.hp_pom_008 import Pom_cl_hp_008
from pytest import mark
from time import sleep

@mark.tc21
def test_TCHP_021(_driver):
    po = Pom_cl_hp_008(_driver)
    po.mouse_hover_latest_collection()
    sleep(10)
    po.screen_shot_capture(r"\HP_016\TCHP021_lat_coll1.jpeg")
    po.click_product_latest_collection()
    sleep(20)
    po.screen_shot_capture(r"\HP_016\TCHP021_lat_coll2.jpeg")
