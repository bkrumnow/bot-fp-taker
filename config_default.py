""" Use this to derive a config.py file. """

import os
from selenium.webdriver.firefox.options import Options

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

IS_MAC_OS = True
FIREFOX_VERSION = "66.0"
GECKODRIVER_VERSION = "0.24.0"
HEADLESS = True
name = None
    
URL = "http://localhost:8080/"
FIREFOX_URL = "https://ftp.mozilla.org/pub/firefox/releases/{}/mac/en-US/Firefox%2066.0.dmg".format(FIREFOX_VERSION)
GECKODRIVER_URL = "http://{}".format(GECKODRIVER_VERSION)

RESOURCE_FOLDER = os.path.join(__location__, 'resources')
FIREFOX_DIR = os.path.join(RESOURCE_FOLDER, 'firefox')
GECKODRIVER_DIR = os.path.join(RESOURCE_FOLDER, 'webdriver')

FIREFOX_BINARY = os.path.join(FIREFOX_DIR, '{}/Firefox.app/Contents/MacOS/firefox'.format(FIREFOX_VERSION))
GECKODRIVER_BINARY = os.path.join(GECKODRIVER_DIR, '{}/geckodriver'.format(GECKODRIVER_VERSION))

BROWSER_MODE = Options()
if HEADLESS:
    BROWSER_MODE.add_argument("--headless")

CONFIGURATION_NAME = name if name else "Firefox_{}_gecko_{}_{}_{}_automated ".format(FIREFOX_VERSION, GECKODRIVER_VERSION, "headless" if HEADLESS else "headful", "macos" if IS_MAC_OS else: "ubuntu")