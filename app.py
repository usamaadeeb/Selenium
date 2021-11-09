import getpass
import os
import logging.handlers
import datetime
import logging
import selenium
from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


baseurl = "https://web.whatsapp.com/"


print(getpass.getuser())


logging.basicConfig(filename='app.log', level=logging.INFO, filemode='a',
                    format='%(asctime)s %(levelname)s  %(message)s %(funcName)s')
logging.basicConfig(filename='app.log', level=logging.ERROR, filemode='a',
                    format='%(asctime)s %(levelname)s  %(message)s %(funcName)s ')

msg = "---Report Sent --- Date: %s" % (datetime.date.today())

file = open('name.txt', 'r')
user = file.readline()


path = open('FilePath.txt', 'r')
path = path.readline()

driverpath = open('DriverPath.txt', 'r')

driverpath = driverpath.readline()
# file.read()
print(user)
opt = webdriver.ChromeOptions()
opt.add_argument(
    '--user-data-dir=/home/usama/.config/google-chrome/Profile 1/')
opt.add_argument('--profile-directory=Profile 1')
print(opt)
# opt.add_argument("--disable-extensions")
browser = webdriver.Chrome(
    executable_path=driverpath, options=opt)

wait = WebDriverWait(browser, 20)

browser.get(baseurl)
time.sleep(8)

browser.maximize_window()
#  time.sleep(8)


def Send_Report():
    x = 1

    return None


Send_Report()

logging.error("Unsuccessful")


try:
    pass
    time.sleep(20)

    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    person_title = wait.until(
        lambda browser: browser.find_element_by_xpath(search_box))
    person_title.clear()
    person_title.send_keys(str(user))
    print(EC.presence_of_element_located(
        browser.find_element_by_xpath(f'//span[@title="{user}"]')))
    user = browser.find_element_by_xpath(f'//span[@title="{user}"]').click()

    msg = "---Report--- Date: %s " % (datetime.date.today)

    time.sleep(18)

    clip = browser.find_element_by_xpath('//span[@data-testid="clip"]').click()

    doc = browser.find_element_by_xpath(
        "//input[@type='file']").send_keys(path)

    time.sleep(5)

    browser.find_element_by_xpath('//span[@data-testid="send"]').click()

    time.sleep(10)

    browser.close()
    logging.info("User: %s --------Successfully---Report Sent --- " %
                 (getpass.getuser()))


except Exception as e:
    logging.error(f"Exception occur - - - - : {e}")
    browser.close()
    print(e)
