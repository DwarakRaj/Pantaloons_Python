from Home_page.generic_functions.selenium_functions import selenium_wrapper
from Home_page.pom_class_files.hp_pom_006 import Pom_cl_hp_006
from selenium.webdriver.common.by import By
class Pom_cl_hp_007(Pom_cl_hp_006, selenium_wrapper):
    whish_list_icon_home_page = (By.XPATH, "//a[@title='Wishlist']")

    def click_on_whish_list_icon(self):
        self.mouse_hover(self.whish_list_icon_home_page)
        self.click_element(self.whish_list_icon_home_page)

