""" Use this to derive a config.py file. """

import os
from selenium.webdriver.firefox.options import Options

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

USE_NIGHTLY = False
IS_MAC_OS = False
FIREFOX_VERSION = "67.0"
GECKODRIVER_VERSION = "0.24.0"
HEADLESS = False
HIDE_WEBDRIVER = False
name = None
    
URL = "http://localhost:8080/"
FIREFOX_URL = "https://ftp.mozilla.org/pub/firefox/releases/{0}/{1}/en-US/Firefox%20{0}.dmg" if IS_MAC_OS else\
	"https://ftp.mozilla.org/pub/firefox/releases/{0}/{1}/en-US/firefox-{0}.tar.bz2"
GECKODRIVER_URL = "https://github.com/mozilla/geckodriver/releases/download/v{0}/geckodriver-v{0}-{1}.tar.gz"

EXTENSION_FOLDER = os.path.join(__location__,'extensions')
EXTENSION = os.path.join(EXTENSION_FOLDER, "stealth_bot.xpi")

RESOURCE_FOLDER = os.path.join(__location__, 'resources')
FIREFOX_DIR = os.path.join(RESOURCE_FOLDER, 'firefox')
GECKODRIVER_DIR = os.path.join(RESOURCE_FOLDER, 'webdriver')

FIREFOX_BINARY = os.path.join(FIREFOX_DIR, '{}/Firefox.app/Contents/MacOS/firefox'.format(FIREFOX_VERSION))
GECKODRIVER_BINARY = os.path.join(GECKODRIVER_DIR, '{}/geckodriver'.format(GECKODRIVER_VERSION))

BROWSER_MODE = Options()
if HEADLESS:
    BROWSER_MODE.add_argument("--headless")

CONFIGURATION_NAME = name if name else "Firefox_{}_gecko_{}_{}_{}_automated".format(
	FIREFOX_VERSION
	, GECKODRIVER_VERSION
	, "headless" if HEADLESS else "headful"
	, "macos" if IS_MAC_OS else "ubuntu"
)
