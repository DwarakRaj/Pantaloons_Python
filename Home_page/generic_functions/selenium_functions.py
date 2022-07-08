from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from PLP_scenaarios.generic_functions.wait_deco import wait
from selenium.webdriver.common.action_chains import ActionChains
class selenium_wrapper:
    reports_ss_path = r"C:\Users\ADMIN\PycharmProjects\Pantaloons_new\Home_page\test_reports"
    def __init__(self,driver):
        self.driver = driver
    @wait #click_element = wait(click_element) #click_element becomes wrapper
    def click_element(self,locator):  #locator--->("class name","ico-register")
        self.driver.find_element(*locator).click() #---> *locator---> "class name","ico-register"
    @wait
    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def select_items(self,locator,value):
        web_el = self.driver.find_element(*locator)
        s = Select(web_el)
        if isinstance(value, str):
            s.select_by_visible_text(value)
        elif isinstance(value, int):
            s.select_by_index(value)
        else:
            raise TypeError
    @wait
    def mouse_hover(self, locator):
        a = ActionChains(self.driver)
        w_btn = self.driver.find_element(*locator)
        a.move_to_element(w_btn).perform()

    def page_down(self):
        a = ActionChains(self.driver)
        a.send_keys(Keys.PAGE_DOWN).perform()


    def screen_shot_capture(self, file_name):
        self.driver.get_screenshot_as_file(self.reports_ss_path+file_name)
