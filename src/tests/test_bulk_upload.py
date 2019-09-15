import os
import time
from selenium.webdriver.common.action_chains import ActionChains


def test_upload_bulk_files(browser):
    browser.get("https://www.perxtech.io/dashboard/signin")
    browser.find_element_by_id("email").send_keys("admin@dashboard.com")
    browser.find_element_by_id("password").send_keys("admin1234")
    browser.find_element_by_xpath("//button[@type='submit']").click()

    action = ActionChains(browser)

    customer_management_wb = browser.find_element_by_xpath("//section/aside/div/ul/li[7]")
    action.move_to_element(customer_management_wb).perform()

    time.sleep(5)
    data_folder_path = os.path.join(os.getcwd(), "src", "data")
    csv_file = os.path.join(data_folder_path, "data.csv")
    txt_file = os.path.join(data_folder_path, "data.txt")
    xlsx_file = os.path.join(data_folder_path, "data.xlsx")
    browser.find_element_by_xpath("//li[@data-key='bulk_actions']/a").click()
    browser.find_element_by_xpath("//button[@class='ant-btn StyledButton-f3xt2-0 dHuLKV ant-btn-primary']").click()
    
    # Upload csv file
    browser.find_element_by_xpath("//span[@class='ant-upload ant-upload-btn']/input[@type='file']").send_keys(csv_file)
    browser.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    browser.refresh()
    time.sleep(1)
    row_id = browser.find_element_by_xpath("//*[@id='root']/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/div[2]").get_attribute("textContent")
    row_num = row_id.split(' ')[1]
    assert browser.find_element_by_xpath("//tr[@data-row-key='{}']/td[2]".format(row_num)).get_attribute("textContent") == "data.csv"

    # Upload txt file
    browser.find_element_by_xpath("//span[@class='ant-upload ant-upload-btn']/input[@type='file']").send_keys(txt_file)
    browser.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    browser.refresh()
    time.sleep(1)
    row_id = browser.find_element_by_xpath("//*[@id='root']/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/div[2]").get_attribute("textContent")
    row_num = row_id.split(' ')[1]
    assert browser.find_element_by_xpath("//tr[@data-row-key='{}']/td[2]".format(row_num)).get_attribute("textContent") == "data.txt"

    # Upload xlsx file
    browser.find_element_by_xpath("//span[@class='ant-upload ant-upload-btn']/input[@type='file']").send_keys(xlsx_file)
    browser.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    browser.refresh()
    time.sleep(1)
    row_id = browser.find_element_by_xpath("//*[@id='root']/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/div[2]").get_attribute("textContent")
    row_num = row_id.split(' ')[1]
    assert browser.find_element_by_xpath("//tr[@data-row-key='{}']/td[2]".format(row_num)).get_attribute("textContent") == "data.xlsx"

