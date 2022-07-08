from Home_page.generic_functions.selenium_functions import selenium_wrapper
from Home_page.pom_class_files.hp_pom_007 import Pom_cl_hp_007
from selenium.webdriver.common.by import By
class Pom_cl_hp_008(Pom_cl_hp_007, selenium_wrapper):
    view_bag = (By.XPATH, "//span[text()='View Bag']")
    cart_icon = (By.XPATH, "//a[@title='Cart']")
    banner_1 = (By.XPATH, "//h3[text()='Must Have Styles of the Season']")
    hp_product = (By.XPATH, "//img[@title='Pastel Pink Waistcoat']")
    pantaloons_logo = (By.XPATH, "//div[@class='pantaloons-logo']//img[@title='Pantaloons']")
    show_recomonds = (By.XPATH, "//img[@class='StyleFinder_style-finder-img__jxsit']")
    latest_collection = (By.XPATH, "//div[@class='MuiGrid-root LatestCollection_latest-collection-grid__3Fqa4 MuiGrid-container']")
    product_lc = (By.XPATH, "//img[@title='Indigo Edit']")

    def click_view_bag(self):
        self.click_element(self.view_bag)

    def mouse_hover_cart_icon(self):
        self.mouse_hover(self.cart_icon)

    def click_on_cart_icon(self):
        self.click_element(self.cart_icon)

    def check_banner1(self):
        self.mouse_hover(self.banner_1)

    def mouse_hover_hp_product(self):
        self.mouse_hover(self.hp_product)

    def click_hp_product(self):
        self.click_element(self.hp_product)

    def click_pantaloons_logo(self):
        self.click_element(self.pantaloons_logo)

    def mouse_hover_show_recomonds(self):
        self.mouse_hover(self.show_recomonds)

    def mouse_hover_latest_collection(self):
        self.mouse_hover(self.latest_collection)

    def click_product_latest_collection(self):
        self.mouse_hover(self.product_lc)
        self.click_element(self.product_lc)


