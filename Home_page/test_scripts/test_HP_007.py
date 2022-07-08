from Home_page.pom_class_files.hp_pom_007 import Pom_cl_hp_007
from pytest import mark
from time import sleep
@mark.tc10
def test_TCHP_010(_driver):
    po = Pom_cl_hp_007(_driver)
    po.click_on_whish_list_icon()
    sleep(8)
    po.screen_shot_capture(r"\HP_007\TCHP_10_whish_list_icon_click.jpeg")

@mark.tc11
def test_TCHP_011(_driver):
    po = Pom_cl_hp_007(_driver)
    po.click_on_whish_list_icon()
    sleep(8)
    po.screen_shot_capture(r"\HP_007\TCHP_11_1_whish_list_icon_before_login.jpeg")
    po.login_process()
    po.click_on_whish_list_icon()
    sleep(8)
    po.screen_shot_capture(r"\HP_007\TCHP_11_2_whish_list_icon_after_lgin.jpeg")

