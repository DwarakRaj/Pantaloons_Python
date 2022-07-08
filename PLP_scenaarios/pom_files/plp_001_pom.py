from PLP_scenaarios.generic_functions.selenium_functions import selenium_wrapper
from selenium.webdriver.common.by import By
from time import sleep
import re
class pm_cl_plp_001(selenium_wrapper):
    women_link = (By.XPATH, "//span[text()='WOMEN']")
    suit_blazer_link = (By.XPATH, "//a[text()='Suits & Blazers']")
    men_link = (By.XPATH, "//div[@class='menu ']//a[@title='MEN']")
    Jeans_link = (By.XPATH, "//a[text()='Jeans']")
    KIDS_link = (By.XPATH, "//div[@class='menu ']//a[@title='KIDS']")
    shirts_link = (By.XPATH, "//a[text()='Shirts']")
    home_decor_link = (By.XPATH, "//div[@class='menu ']//a[@title='HOME DECOR']")
    table_acces_link = (By.XPATH, "//a[text()='Table Accessories']")
    accessories_link = (By.XPATH, "//div[@class='menu ']//a[@title='ACCESSORIES']")
    women_shoes_link = (By.XPATH, "//a[@title='WOMEN FOOTWEAR']/../..//a[text()='Sneakers & Sports Shoes']")
    load_more_btn = (By.XPATH, "//div[text()='LOAD MORE']")
    displayed_items_xpath = (By.XPATH, "//div[@class='PlpWeb_product-price__2A3Lf']")
    count_displayed_xpath = (By.XPATH, "//div[@class='PlpWeb_products-count__38RjJ']")
    product_type = (By.XPATH, "//p[text()='Product Type']")
    Bottles_ = (By.XPATH, "//div[text()='Bottle (15)']")
    Coaster_link = (By.XPATH, "//div[text()='Coaster (5)']")
    Farmal_Trousers_link = (By.XPATH, "//a[text()='Formal Trousers']")
    item_farmal_trouser = (By.XPATH, "//div[text()='Peter England']")
    def mouse_hov_kids(self):
        self.mouse_hover(self.KIDS_link)
        self.mouse_hover(self.shirts_link)

    def click_shirts_link(self):
        self.click_element(self.shirts_link)

    def mouse_hov_men(self):
        self.mouse_hover(self.men_link)


    def click_Jeans_link(self):
        self.mouse_hover(self.Jeans_link)
        self.click_element(self.Jeans_link)

    def mouse_hov_women(self):
        self.mouse_hover(self.women_link)
        self.mouse_hover(self.suit_blazer_link)

    def click_suit_blazer_item(self):
        self.click_element(self.suit_blazer_link)


    def mouse_hov_home_decor(self):
        self.mouse_hover(self.home_decor_link)
        self.mouse_hover(self.table_acces_link)


    def click_table_acces_link(self):
        self.click_element(self.table_acces_link)

    def mouse_hover_accessories(self):
        self.mouse_hover(self.accessories_link)
        self.mouse_hover(self.women_shoes_link)

    def click_women_shoes_link(self):
        self.click_element(self.women_shoes_link)

    def count_products_bottles(self):
        self.click_element(self.product_type)
        self.click_element(self.Bottles_)
        sleep(5)
        actual_item_count = len(self.driver.find_elements(*self.displayed_items_xpath))
        display_item_count = int("".join(re.findall("\d", self.driver.find_element(*self.count_displayed_xpath).text)))
        return actual_item_count, display_item_count

    def count_products_coaster(self):
        self.click_element(self.product_type)
        self.click_element(self.Coaster_link)
        sleep(5)
        actual_item_count = len(self.driver.find_elements(*self.displayed_items_xpath))
        display_item_count = int("".join(re.findall("\d", self.driver.find_element(*self.count_displayed_xpath).text)))
        return actual_item_count, display_item_count


    def click_Farmal_trousers(self):
        self.click_element(self.Farmal_Trousers_link)

    def mouse_hover_item_Farmal_trousers(self):
        self.mouse_hover(self.item_farmal_trouser)