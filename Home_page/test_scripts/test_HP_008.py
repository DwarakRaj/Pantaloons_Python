from Home_page.pom_class_files.hp_pom_008 import Pom_cl_hp_008
from pytest import mark
from time import sleep
@mark.tc12
def test_TCHP_012(_driver):
    po = Pom_cl_hp_008(_driver)
    po.mouse_hover_cart_icon()
    po.screen_shot_capture(r"\HP_008\TCHP12_before_login.jpeg")
    po.login_process()
    sleep(8)
    po.mouse_hover_cart_icon()
    sleep(8)
    po.screen_shot_capture(r"\HP_008\TCHP12_after_login.jpeg")
    po.click_view_bag()
    sleep(8)
    po.screen_shot_capture((r"\HP_008\TCHP12_cart_page.jpeg"))

@mark.tc14
def test_TCHP_013(_driver):
    po = Pom_cl_hp_008(_driver)
    sleep(10)
    po.page_down()
    sleep(4)
    po.screen_shot_capture()