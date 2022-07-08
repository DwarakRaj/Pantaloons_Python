from Home_page.generic_functions.selenium_functions import selenium_wrapper
from selenium.webdriver.common.by import By
from time import sleep
import re
class Pom_cl_hp_001_002(selenium_wrapper):
    women_link = (By.XPATH, "//span[text()='WOMEN']")
    men_link = (By.XPATH, "//div[@class='menu ']//a[@title='MEN']")
    KIDS_link = (By.XPATH, "//div[@class='menu ']//a[@title='KIDS']")
    home_decor_link = (By.XPATH, "//div[@class='menu ']//a[@title='HOME DECOR']")
    accessories_link = (By.XPATH, "//div[@class='menu ']//a[@title='ACCESSORIES']")
    brands_link = (By.XPATH, "//div[@class='menu selected-menu-border']//a[@title='BRANDS']")


    def mouse_hov_men(self):
        self.mouse_hover(self.men_link)

    def mouse_hov_women(self):
        self.mouse_hover(self.women_link)

    def mouse_hov_kids(self):
        self.mouse_hover(self.KIDS_link)

    def mouse_hov_home_decor(self):
        self.mouse_hover(self.home_decor_link)

    def mouse_hover_accessories(self):
        self.mouse_hover(self.accessories_link)

    def mouse_hover_brands(self):
        self.mouse_hover(self.brands_link)

