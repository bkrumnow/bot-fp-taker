""" bot that takes produces a fingerprint with the current browser and . """
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains

from setup import set_up_environment

from config import GECKODRIVER_BINARY
from config import FIREFOX_BINARY
from config import URL
from config import CONFIGURATION_NAME
from config import BROWSER_MODE


set_up_environment()

driver = webdriver.Firefox(executable_path=GECKODRIVER_BINARY, firefox_binary=FIREFOX_BINARY, firefox_options = BROWSER_MODE)
try: 
    driver.get(URL)
except Exception:
    raise Exception("Could not connect. Is the fingerprint server running?")

INPUT_ID = "txtConfDesc"
SUBMIT_BTN_ID = "btnFP"
input_field = driver.find_element_by_id(INPUT_ID)
submit_btn = driver.find_element_by_id(SUBMIT_BTN_ID)

try:
    actions = ActionChains(driver)
    actions.move_to_element(input_field).click(input_field).send_keys(CONFIGURATION_NAME).send_keys(Keys.TAB).send_keys(Keys.RETURN).perform()
    time.sleep(3)
    alert = driver.switch_to_alert()
    alert.accept()
    print("Fingerprint taken for {}".format(CONFIGURATION_NAME))
except Exception as e:
    print("Error executing the interaction:\n {}".format(e))
finally:
    driver.close()