import os

from selenium.webdriver.common.action_chains import ActionChains

from src.pages.base_page import BasePage
from src.pages.admin_page import AdminPage

class BulkActionPage(BasePage):

    UPLOAD_BUTTON = "//button[@class='ant-btn StyledButton-f3xt2-0 dHuLKV ant-btn-primary']"
    UPLOAD_DRAG_BUTTON = "//div[@class='ant-upload-drag-container']"
    POP_UP_UPLOAD_BUTTON = "//div[@class='ant-modal-footer']/button[@class='ant-btn ant-btn-primary']"

    def start(self):
        self.url = "/p/bulkaction"
