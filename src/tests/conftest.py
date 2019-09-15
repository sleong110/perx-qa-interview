import json
import pytest

from selenium.webdriver import Chrome

CONFIG_PATH = 'src/tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome'] # For future cross browser testing purpose

@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else 10

@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == 'chrome':
        driver = Chrome()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    
    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()