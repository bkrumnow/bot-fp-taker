""" bot that takes produces a fingerprint with the current browser and . """
import os

from config import FIREFOX_VERSION
from config import GECKODRIVER_VERSION
from config import RESOURCE_FOLDER
from config import FIREFOX_DIR
from config import GECKODRIVER_DIR
from config import FIREFOX_URL
from config import GECKODRIVER_URL
from config import FIREFOX_BINARY
from config import GECKODRIVER_BINARY

from config import IS_MAC_OS

import pdb

def does_exist(file_with_path):
    """Checks if a file exists """
    return os.path.isfile(file_with_path)

def set_up_firefox():
    """ Downloads Firefox """
    print("Downloading Firefox {}".format(FIREFOX_VERSION))
    status = os.system("wget -O target.dmg {}".format(FIREFOX_URL))
    if status != 0:
        raise Exception("Could not download Firefox.")
    
    #OS-Specific?
    os.system("hdiutil attach -nobrowse -mountpoint /Volumes/firefox-tmp target.dmg")
    
    path = os.path.join(FIREFOX_DIR, FIREFOX_VERSION)
    os.system("mkdir {}".format(path))
    os.system("cp -r /Volumes/firefox-tmp/Firefox.app {}/Firefox.app".format(path))
    os.system("hdiutil detach /Volumes/firefox-tmp")
    os.system("rm target.dmg")

def set_up_geckodriver():
    """ Downloads the files Geckodriver """
    print("Downloading Firefox {}".format(GECKODRIVER_VERSION))
    OS_STRING = "macos"
    #OS specific in any case. Apply both to ubuntu!
    status = os.system("wget -O geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v{0}/geckodriver-v{0}-{1}.tar.gz".format(GECKODRIVER_VERSION, OS_STRING))
    if status != 0:
        raise Exception("Could not download Geckodriver.")
    
    
    path = os.path.join(GECKODRIVER_DIR, GECKODRIVER_VERSION)
    os.system("mkdir {}".format(path))
    os.system("tar -C {} -xzf geckodriver.tar.gz".format(path))
    # also introduce commad to move geckodriver to the correct path
    os.system("rm geckodriver.tar.gz")
    

def set_up_environment():
    if not does_exist(FIREFOX_BINARY):
        set_up_firefox()
    
    if not does_exist(GECKODRIVER_BINARY):
        set_up_geckodriver()
