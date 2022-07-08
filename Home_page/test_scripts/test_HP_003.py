from Home_page.pom_class_files.hp_pom_003 import Pom_cl_hp_003
from pytest import mark
from time import sleep
@mark.tc2
def test_TCHP_003(_driver):
    po = Pom_cl_hp_003(_driver)
    sleep(5)
    po.mouse_hov_women()
    sleep(5)
    po.screen_shot_capture(r"\HP_003\TCHP_women.jpeg")
    po.mouse_hov_men()
    sleep(5)
    po.screen_shot_capture(r"\HP_003\TCHP_men.jpeg")
    po.mouse_hov_kids()
    sleep(5)
    po.screen_shot_capture(r"\HP_003\TCHP_kids.jpeg")
    po.mouse_hov_home_decor()
    sleep(5)
    po.screen_shot_capture(r"\HP_003\TCHP_home_decor.jpeg")
    po.mouse_hover_accessories()
    sleep(5)
    po.screen_shot_capture(r"\HP_003\TCHP_home_decor.jpeg")
    po.mouse_hover_brands()
    sleep(8)
    po.screen_shot_capture(r"\HP_003\TCHP_brands.jpeg")

@mark.tc4
def test_TCHP_004(_driver):
    po = Pom_cl_hp_003(_driver)
    po.click_women_link()
    sleep(10)
    po.screen_shot_capture(r"\HP_003\TCHP_004_women.jpeg")
    po.click_men_link()
    sleep(10)
    po.screen_shot_capture(r"\HP_003\TCHP_004_men.jpeg")
    po.click_kids_link()
    sleep(10)
    po.screen_shot_capture(r"\HP_003\TCHP_004_kids.jpeg")
    po.click_home_decor()
    sleep(10)
    po.screen_shot_capture(r"\HP_003\TCHP_004_home_decor.jpeg")
    sleep(10)
    po.click_accessories()
    sleep(10)
    po.screen_shot_capture(r"\HP_003\TCHP_004_acceessories.jpeg")
    po.click_brands()
    sleep(10)
    po.screen_shot_capture(r"\HP_003\TCHP_004_brands.jpeg")


@mark.tc5
def test_TCHP_005(_driver):
    po = Pom_cl_hp_003(_driver)
    po.mouse_hov_women()
    po.mouse_hover_new_arriv_img_women()
    sleep(8)
    po.screen_shot_capture(r"\HP_003\TCHO_005_women.jpeg")
    po.mouse_hov_men()
    sleep(4)
    po.mouse_hover_new_arriv_img_men()
    sleep(8)
    po.screen_shot_capture(r"\HP_003\TCHP_005_men.jpeg")
    po.mouse_hov_kids()
    sleep(3)
    po.mouse_hover_new_arriv_img_kids()
    sleep(8)
    po.screen_shot_capture(r"\HP_003\TCHP_005_kids.jpeg")

