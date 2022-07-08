from Home_page.generic_functions.selenium_functions import selenium_wrapper
from Home_page.pom_class_files.hp_pom_005 import Pom_cl_hp_005
from selenium.webdriver.common.by import By
from time import sleep
class Pom_cl_hp_006(Pom_cl_hp_005, selenium_wrapper):
    my_account_icon = (By.XPATH, "//a[@title='My Account']")
    mobile_num_text_field = ((By.XPATH, "//input[@placeholder='Mobile Number']"), "8886213059")
    get_otp_btn = (By.XPATH, "//span[text()='Get OTP']")
    submit_otp_btn = (By.XPATH, "//span[text()='Start Shopping']")
    orders = (By.XPATH, "//li[text()='ORDERS']")
    whish_list = (By.XPATH, "//li[text()='WISHLIST']")
    profile_details = (By.XPATH, "//li[text()='PROFILE DETAILS']")
    addresses = (By.XPATH, "//li[text()='ADDRESSES']")
    pantaloons_credit = (By.XPATH, "//li[text()='PANTALOONS CREDIT']")
    green_card = (By.XPATH, "//li[text()='GREENCARD']")
    log_out = (By.XPATH, "//li[text()='LOG OUT']")

    def mouse_hover_face_icon(self):
        self.mouse_hover(self.my_account_icon)

    def click_my_account_icon(self):
        self.click_element(self.my_account_icon)

    def click_on_orders(self):
        self.mouse_hover(self.orders)
        self.click_element(self.orders)

    def click_on_whish_list(self):
        self.mouse_hover(self.whish_list)
        self.click_element(self.whish_list)

    def click_on_profile_details(self):
        self.mouse_hover(self.profile_details)
        self.click_element(self.profile_details)

    def click_on_address(self):
        self.mouse_hover(self.addresses)
        self.click_element(self.addresses)

    def click_on_pantaloons_credit(self):
        self.mouse_hover(self.pantaloons_credit)
        self.click_element(self.pantaloons_credit)

    def click_on_green_card(self):
        self.mouse_hover(self.green_card)
        self.click_element(self.green_card)

    def click_on_log_out(self):
        self.mouse_hover(self.log_out)
        self.click_element(self.log_out)

    def login_process(self):
        self.click_my_account_icon()
        sleep(8)
        self.enter_text(self.mobile_num_text_field[0], self.mobile_num_text_field[1])
        self.click_element(self.get_otp_btn)
        sleep(10)
        self.click_element(self.submit_otp_btn)
