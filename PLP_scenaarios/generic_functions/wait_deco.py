from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep
from selenium.webdriver.remote.webelement import WebElement

class element_visible_enable_check(visibility_of_element_located):
    def __call__(self,locat_):
        displayed = super().__call__(locat_)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        instan_ = args[0]
        locat_ = args[1]
        sleep(5)
        wait = WebDriverWait(instan_.driver,50)
        # v = visibility_of_element_located(locat_)
        v = element_visible_enable_check(locat_)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper
