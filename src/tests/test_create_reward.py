import pytest

from src.pages.login_page import LoginPage
from src.pages.reward_admin_page import RewardAdminPage

def test_cannot_access_reward_page_directly(browser):
    """
    GIVEN user wants to go to reward page directly with reward url
    WHEN user key in reward page url directly in the browser
    THEN user will be redirect to login page
    """
    reward_admin_page = RewardAdminPage(browser)    
    reward_admin_page.load(reward_admin_page.url)

    # Check that when user try to access reward admin page \
    # the user will be redirect to login page.
    assert reward_admin_page.get_id(LoginPage.EMAIL_CONTAINER).size !=0
    assert reward_admin_page.get_id(LoginPage.PASSWORD_CONTAINER).size !=0
    assert reward_admin_page.get_xpath(LoginPage.LOGIN_BUTTON).size !=0


def test_create_reward(browser):
    """
    GIVEN user wants to login to reward page as reward admin
    WHEN user keys in correct email address and password 
    THEN user is logged in as reward admin
    AND reward admin can create reward
    """

    login_page = LoginPage(browser)
    login_page.login(email="reward_admin@dashboard.com",
                    password="reward_admin")
    
    reward_admin_page = RewardAdminPage(browser)
    reward_admin_page.start()

    result = reward_admin_page.create_new_reward()
    assert reward_admin_page.get_xpath(RewardAdminPage.REWARD_FORM_STATUS).get_attribute('textContent') == "ACTIVE"
