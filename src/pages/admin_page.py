from .base_page import BasePage

class AdminPage(BasePage):

    # Xpath of menu items
    REPORTS_MENU_ITEM = "//li[@data-key='reports']"
    REWARDS_MENU_ITEM = "//li[@data-key='rewards']"
    CAMPAIGNS_MENU_ITEM = "//li[@data-key='campaigns']"
    LOYALTIES_MENU_ITEM = "//li[@data-key='loyalties']"
    TRANSACTION_RULES_MENU_ITEM = "//li[@data-key='transaction_rules']"
    MERCHANTS_MENU_ITEM = "//li[@data-key='merchants']"
    CUSTOMER_MANAGEMENT_MENU_ITEM = "//li[@data-key='customer_management']"
    SETTINGS_MENU_ITEM = "//li[@data-key='settings']"
    BUSINESS_INTELLIGENCE_MENU_ITEM = "//li[@data-key='business_intelligence']"
    BULK_ACTION_LINK = "//ul[@id='customer_management$Menu']/li[@data-key='bulk_actions']/a"
    BULK_ACTION_SUBMENU = "//li[@data-key='customer_management']/div[@class='ant-menu-submenu-title']"
    CUSTOMER_MANAGEMENT_ICON = "//i[@src='customers']"

    def start(self):
        self.url = "/p/reports/downloads"
        
        
    def get_side_bar_menu_item(self, xpath):
        return self.get_xpath(xpath)