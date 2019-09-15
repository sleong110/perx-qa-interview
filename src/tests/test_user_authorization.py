import pytest

from selenium.common.exceptions import NoSuchElementException

from src.pages.admin_page import AdminPage
from src.pages.login_page import LoginPage
from src.pages.reward_admin_page import RewardAdminPage

def test_admin_user_login(browser):
    """
    GIVEN user is asked to login via dashbord
    WHEN user login as admin user
    THEN perx main page with all functions in side bar is displayed
    """
    login_page = LoginPage(browser)
    login_page.start()

    login_page.login(email="admin@dashboard.com",
                    password="admin1234")
    admin_page = AdminPage(browser)
    admin_page.start()

    # Check that admin has sufficient right to access all functionality 
    assert admin_page.get_side_bar_menu_item(AdminPage.REPORTS_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.REWARDS_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.CAMPAIGNS_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.LOYALTIES_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.TRANSACTION_RULES_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.MERCHANTS_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.CUSTOMER_MANAGEMENT_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.SETTINGS_MENU_ITEM).size != 0
    assert admin_page.get_side_bar_menu_item(AdminPage.BUSINESS_INTELLIGENCE_MENU_ITEM).size != 0

def test_reward_user_login(browser):
    """
    GIVEN user is asked to login via dashbord
    WHEN user login as reward user
    THEN perx main page with ONLY reward priviledge is displayed
    """

    login_page = LoginPage(browser)
    login_page.start()

    login_page.login(email="reward_admin@dashboard.com",
                    password="reward_admin")
    
    reward_admin_page = RewardAdminPage(browser)
    reward_admin_page.start()

    # Check that reward_admin has can only have priviledge to create reward
    assert reward_admin_page.get_side_bar_menu_item(RewardAdminPage.REWARDS_MENU_ITEM).size != 0

    # Check that rest of the menu_item element that can be found in admin page cannot be found in
    # reward admin page
    with pytest.raises(NoSuchElementException):
        reward_admin_page.get_side_bar_menu_item(AdminPage.REPORTS_MENU_ITEM)
        reward_admin_page.get_side_bar_menu_item(AdminPage.CAMPAIGNS_MENU_ITEM) 
        reward_admin_page.get_side_bar_menu_item(AdminPage.LOYALTIES_MENU_ITEM) 
        reward_admin_page.get_side_bar_menu_item(AdminPage.TRANSACTION_RULES_MENU_ITEM) 
        reward_admin_page.get_side_bar_menu_item(AdminPage.MERCHANTS_MENU_ITEM) 
        reward_admin_page.get_side_bar_menu_item(AdminPage.CUSTOMER_MANAGEMENT_MENU_ITEM) 
        reward_admin_page.get_side_bar_menu_item(AdminPage.SETTINGS_MENU_ITEM) 
        reward_admin_page.get_side_bar_menu_item(AdminPage.BUSINESS_INTELLIGENCE_MENU_ITEM)
