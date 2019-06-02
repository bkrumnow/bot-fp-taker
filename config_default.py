""" Use this to derive a config.py file. """

import os
from selenium.webdriver.firefox.options import Options

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
URL = "http://localhost:8080/"
RESOURCE_FOLDER = os.path.join(__location__, 'resources')
DIR_GECKO_DRIVER = os.path.join(RESOURCE_FOLDER, 'webdriver/geckodriver')
DIR_FIREFOX_BINARY = os.path.join(RESOURCE_FOLDER, 'browser/Firefox.app/Contents/MacOS/firefox')

FIREFOX_VERSION = "66.0"
GECKODRIVER_VERSION = "0.24.0"

#headless mode on?
HEADLESS = True
# Set up a specific name to appear in the fingerprint database
name = "FX_nightly_67.0_64-bit_headless_automated_noOpenWPM"


MODE = Options()
if HEADLESS:
    MODE.add_argument("--headless")

CONFIGURATION = name if name else "Firefox_{}_gecko_{}_{} ".format(FIREFOX_VERSION, GECKODRIVER_VERSION, "headless" if HEADLESS else "headful")