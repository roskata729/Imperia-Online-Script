from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import attacks.dungeon as dungeon
import farming.vassals as vassals
import utilities.login as loginManager
import time

username = loginManager.getUsernameFromInput()
password = loginManager.getPasswordFromInput()

options = Options()
# options.add_argument('-headless')  # uncomment for final version so that it works without GUIz`

driver = webdriver.Chrome(options=options)



loginManager.loginToImperiaOnlineWithGivenCredentials(driver, username, password)

dungeon.sendDungeonAttacks(driver)

vassals.collectVassalGold(driver)

time.sleep(5)
driver.quit()