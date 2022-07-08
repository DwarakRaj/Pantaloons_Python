from Home_page.generic_functions.selenium_functions import selenium_wrapper
from Home_page.pom_class_files.hp_pom_001_002 import Pom_cl_hp_001_002
from selenium.webdriver.common.by import By
from time import sleep
import re
class Pom_cl_hp_003(Pom_cl_hp_001_002, selenium_wrapper):
    sub_cat_img_women = (By.XPATH, "//img[@alt='Jeans']")
    sub_cat_img_men = (By.XPATH, "//img[@alt='T-shirts']")
    sub_cat_img_kids = (By.XPATH, "//img[@alt='Active wear']")
    casual_options_sbo_women = (By.XPATH, "//div[text()='Casual']")
    work_wear_option_sbo_men = (By.XPATH, "//div[text()='Work Wear']")
    festive_opttin_sbo_kids = (By.XPATH, "//div[text()='Festive']")

    def click_women_link(self):
        self.click_element(self.women_link)

    def click_men_link(self):
        self.click_element(self.men_link)

    def click_kids_link(self):
        self.click_element(self.KIDS_link)

    def click_home_decor(self):
        self.click_element(self.home_decor_link)

    def click_accessories(self):
        self.click_element(self.accessories_link)

    def click_brands(self):
        self.click_element(self.brands_link)

    def mouse_hover_new_arriv_img_women(self):
        self.mouse_hover(self.sub_cat_img_women)
        sleep(3)
        self.click_element(self.sub_cat_img_women)

    def mouse_hover_new_arriv_img_men(self):
        self.mouse_hover(self.sub_cat_img_men)
        sleep(3)
        self.click_element(self.sub_cat_img_men)

    def mouse_hover_new_arriv_img_kids(self):
        self.mouse_hover(self.sub_cat_img_kids)
        sleep(3)
        self.click_element(self.sub_cat_img_kids)

