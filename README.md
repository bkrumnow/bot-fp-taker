# bot-fp-taker

## Description
The goal of this project is to automated the process of taking fingerprints of web bots. 
Automatically deploys Selenium-Webdriver-based bots to take fingerprints. 
Assumes that an fp-server instance is running (see also https://github.com/bkrumnow/BrowserBasedBotFP) 

Only Geckodriver with Firefox is currently supported. 


## Installation
This project uses python 3.
Install a Selenium version of your choice. By default Selenium 3.141 is used:
  
  `pip install -r requirements.txt`

Duplicate the config_default.py and name it config.py. Adjust the following fields:

* `IS_MAC_OS`: Set to true, if a Macintosh is used. Otherwise Ubuntu as underlying OS is assumed.
* `FIREFOX_VERSION`: The Firefox version that shall be tested, e.g. 67.0.1 
* `GECKODRIVER_VERSION`: Geckodriver version that shall be used, e.g. "0.24.0"
* `HEADLESS`: Headless mode on/off
* `name (default: None)`: Set for a custom string. By default it uses a string consisting of Firefox version, Geckodriver   version, OS string and headless mode  

Build the stealth extension with:

  `make -F Makefile`
  
## Usage
run with:

  `python fp_factory.py`
