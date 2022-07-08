from Home_page.generic_functions.selenium_functions import selenium_wrapper
from Home_page.pom_class_files.hp_pom_003 import Pom_cl_hp_003
from selenium.webdriver.common.by import By
class Pom_cl_hp_004(Pom_cl_hp_003, selenium_wrapper):
    casual_options_sbo_women = (By.XPATH, "//div[text()='Casual']")
    work_wear_option_sbo_men = (By.XPATH, "//div[text()='Work Wear']")
    festive_opttin_sbo_kids = (By.XPATH, "//div[text()='Festive']")

    def shop_by_occation_women(self):
        self.mouse_hover(self.casual_options_sbo_women)
        self.click_element(self.casual_options_sbo_women)

    def shop_by_occation_men(self):
        self.mouse_hover(self.work_wear_option_sbo_men)
        self.click_element(self.work_wear_option_sbo_men)

    def shop_by_occation_kids(self):
        self.mouse_hover(self.festive_opttin_sbo_kids)
        self.click_element(self.festive_opttin_sbo_kids)




