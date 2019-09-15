from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class RewardAdminPage(BasePage):

    # Xpath of menu items
    REWARDS_MENU_ITEM = "//li[@data-key='rewards']"
    CREATE_NEW_BUTTON = "//button[@class='ant-btn StyledButton-f3xt2-0 dHuLKV ant-btn-primary']"
    FORM_NEXT_BUTTON = "//button[@class='ant-btn StyledButton-f3xt2-0 dHuLKV ant-btn-primary']"
    VALIDITY_PERIOD_TEXT_BOX = "//div/input[@placeholder='Select date']"
    VALIDITY_PERIOD = "//section[@class='sc-fzXfLU cwnznC']"
    SUBMIT_BUTTON = "//button[@type='submit']"
    REWARD_FORM_STATUS = "//section[@class='sc-fzXfLV itFpkU']/span[@class='ant-tag ant-tag-has-color']"

    def start(self):
        self.url = "/p/rewards/list"

    def get_side_bar_menu_item(self, xpath):
        return self.get_xpath(xpath)
    
    def create_new_reward(self):
        self.click_button(RewardAdminPage.CREATE_NEW_BUTTON)
        self.click_button(RewardAdminPage.FORM_NEXT_BUTTON)
        validity_period_text_box = self.get_multi_xpaths(RewardAdminPage.VALIDITY_PERIOD_TEXT_BOX)

        try:
            for i in range(len(validity_period_text_box)):
                if validity_period_text_box[i].get_attribute('value'):
                    pass
                else:
                    validity_period_text_box[i].send_keys('2010-10-10')
        except Exception as e:
            print(validity_period_text_box[0].get_attribute('value'))
            print(validity_period_text_box[1].get_attribute('value'))
            raise e

        self.click_button(RewardAdminPage.FORM_NEXT_BUTTON)
        self.click_button(RewardAdminPage.SUBMIT_BUTTON)
