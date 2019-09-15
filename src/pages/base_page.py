import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, browser, base_url="https://www.perxtech.io/dashboard"):
        self.base_url = base_url
        self.browser = browser
        self.start()
    
    def get_title(self):
        return self.browser.title

    def load(self, url):
        url = self.base_url + url
        self.browser.get(url)
    
    def get_xpath(self, xpath):
        """ Return DOM element of the xpath
        """
        return self.browser.find_element_by_xpath(xpath)
    
    def get_multi_xpaths(self, xpath):
        return self.browser.find_elements_by_xpath(xpath)

    def get_id(self, id):
        """ Return DOM element of the id
        """
        return self.browser.find_element_by_id(id)
    
    def get_tag(self, tag):
        """ Return DOM element of the tag
        """
        return self.browser.find_element_by_tag(tag)

    def click_button(self, xpath):
        return self.browser.find_element_by_xpath(xpath).click()
    
    def send_text_by_id(self, id, text):
        self.browser.find_element_by_id(id).send_keys(text)
    
    def send_text_by_xpath(self, xpath, text):
        self.browser.find_element_by_xpath(xpath).send_keys(text)
    
    def execute_script(self, command, text):
        self.browser.execute_script(command, text)
    
    def get_pop_up_window_title(self, window_handle):
        self.browser.switch_to.window(window_handle)

    def mouse_hover(self, xpath):
        return ActionChains(self.browser).move_to_element(self.browser.find_element_by_xpath(xpath)).perform()

    def wait(self, seconds):
        time.sleep(seconds)
    
    def go_back(self):
        self.browser.back()