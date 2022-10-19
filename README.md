# Messenger Test Personal Project - ongoing
Test automation on eBay messaging system. This is functional testing on the user messaging module. The automation scripts follow the page object model. It is built using selenium web driver and pytest. 
* [test scenarios and test cases](https://docs.google.com/spreadsheets/d/1X-XO-Q_YnWaXMrCdl4BSfNUA54AbHEzLCps6emL-yH4/edit?usp=sharing)
* [test/defects report](https://docs.google.com/spreadsheets/d/1NbceW92K4iyatiAroCZX4PzXQpn0KJmIBy2pSAjAYU8/edit#gid=0)

As a long-term member of eBay, I encounter several usability issues and small bugs when I'm using the application(both web and mobile). So I decided to do a testing project to practice automated testing and manual testing.
## Getting Started

### Install/reinstall the new version of selenium drivers

1. Download the same versions of web driver as your current  browser version </br>
   chrome link: https://chromedriver.chromium.org/downloads
2. Add driver file to your path </br>
   ref: https://github.com/SeleniumHQ/selenium/tree/trunk/py)
3. For Mac, it may fail to use the driver because the developer is not verified. So execute this line on terminal.
    ```
    xattr -d com.apple.quarantine /usr/local/bin/chromedriver
   ```
    </br>
   ref: https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de

### Run automation scripts
1. Edit the config file with your user information(username and password)
2. Run the login.py to save the cookies for user login.
3. Run test cases script. You can edit and run with different test data.

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>
