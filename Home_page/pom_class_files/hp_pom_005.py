from Home_page.generic_functions.selenium_functions import selenium_wrapper
from Home_page.pom_class_files.hp_pom_004 import Pom_cl_hp_004
from selenium.webdriver.common.by import By
class Pom_cl_hp_005(Pom_cl_hp_004, selenium_wrapper):
    women_brand_logo = (By.XPATH, "//img[@title='Akkriti']")
    men_brand_logo = (By.XPATH, "//img[@title='Indus Route']")
    kids_brand_logo = (By.XPATH, "//img[@title='Mini Klub']")

    def click_women_brand(self):
        self.mouse_hover(self.women_brand_logo)
        self.click_element(self.women_brand_logo)

    def click_men_brand(self):
        self.mouse_hover(self.men_brand_logo)
        self.click_element(self.men_brand_logo)

    def click_kids_brand(self):
        self.mouse_hover(self.kids_brand_logo)
        self.click_element(self.kids_brand_logo)