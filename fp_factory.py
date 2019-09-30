""" bot that takes produces a fingerprint with the current browser and . """
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from setup import set_up_environment

from config import GECKODRIVER_BINARY
from config import FIREFOX_BINARY
from config import URL
from config import CONFIGURATION_NAME
from config import BROWSER_MODE
from config import EXTENSION
from config import HIDE_WEBDRIVER
from config import EXPERIMENT


def run():
    set_up_environment()
    print(GECKODRIVER_BINARY)
    driver = webdriver.Firefox(executable_path=GECKODRIVER_BINARY, firefox_binary=FIREFOX_BINARY, firefox_options = BROWSER_MODE)

    #injects the firefox extension to overwride web driver specifc variables
    if HIDE_WEBDRIVER:
        driver.install_addon(EXTENSION, temporary=True)
    
    try: 
        driver.get(URL)
    except Exception:
        raise Exception("Could not connect. Is the fingerprint server running?")

    if EXPERIMENT == "SLG19":
        run_SLG19(driver, CONFIGURATION_NAME)
    elif EXPERIMENT == "JKV19":
        run_JKV19(driver, CONFIGURATION_NAME)
    else:
        run_openwpm_detector(driver)


def run_openwpm_detector(driver):
    try:        
        """ clicks the button in order to start fingerprinting """
        time.sleep(5)
        el = driver.find_element_by_id("detect")
        action = ActionChains(driver)
        action.move_to_element(el).click(el).perform()
        time.sleep(6)
        driver.save_screenshot("screenshot.png")
        ele = driver.find_element_by_css_selector("body")
        print(ele.get_attribute('innerHTML'))
    except Exception as e:
        print("Error executing the interaction:\n {}".format(e))
    finally:
        driver.close()

def run_SLG19(driver, text):
    try:        
        """ clicks the button in order to start fingerprinting """
        time.sleep(5)
        el = driver.find_element_by_css_selector("input")
        action = ActionChains(driver)
        action.move_to_element(el).click(el).perform()
        time.sleep(3)
        alert = driver.switch_to_alert()
        alert.send_keys(text)
        time.sleep(2)
        alert.accept()
        time.sleep(7)
    except Exception as e:
        print("Error executing SLG19 interaction:\n {}".format(e))
    finally:
        driver.close()    

def run_JKV19(driver, text):
    INPUT_ID = "txtConfDesc"
    SUBMIT_BTN_ID = "btnFP"
    input_field = driver.find_element_by_id(INPUT_ID)
    submit_btn = driver.find_element_by_id(SUBMIT_BTN_ID)
    
    try:
        actions = ActionChains(driver)
        time.sleep(1)
        actions.move_to_element(input_field).click(input_field).send_keys(text).send_keys(Keys.TAB).send_keys(Keys.RETURN).perform()
        time.sleep(3)
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(2)
        print("Fingerprint taken for {}".format(text))
    except Exception as e:
        print("Error executing JKV19 interaction:\n {}".format(e))
    finally:
        driver.close()

if __name__ == "__main__":
    run()
