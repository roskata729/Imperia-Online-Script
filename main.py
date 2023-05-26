from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import threading
import json
import getpass

def sendDungeonAttacks():
    # Checks if activity popup is shown and closes it
    if driver.find_element("xpath",'//*[@class="txt-title"]'):
        driver.find_element("xpath",'//*[@title="Затваряне"]').click()

    try: 

        dungeon = driver.find_element("xpath",'//*[@class="canvas-node dungeon-light"]')


        # Create an ActionChains object
        actions = ActionChains(driver)
        # Move to the dungeon and click it
        actions.move_to_element(dungeon).click().perform()
        time.sleep(2)
        dungeon_attack_button = driver.find_element("name", "attack")
        # Check if you have available attacks
        if dungeon_attack_button:
            if dungeon_attack_button.is_enabled:
                dungeon_attack_button.click()
                time.sleep(2)
                #driver.find_element("xpath",'//*[@class="flanks-flank-archers"]')
                #driver.find_element("id", "attack-general").click()
                time.sleep(1)
                driver.find_element("id", "select-all-army").click()
                time.sleep(1)
                sendAttackButton = driver.find_element("xpath", '//*[@value="Полева Битка"]') or driver.find_element("xpath", '//*[@value="Крепостна Обсада"]')
                sendAttackButton.click()
    except NoSuchElementException:
        print("В момента няма налични безплатни атаки")

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

options = Options()
# options.add_argument('-headless')  # uncomment for final version so that it works without GUIz`

driver = webdriver.Chrome(options=options)

driver.get("https://www122.imperiaonline.org/")

time.sleep(2)
# # find username/email field and send the username itself to the input field
driver.find_element("id", "login-user").send_keys(username)
driver.find_element("id", "login-pass").send_keys(password)
driver.find_element("name", "image-submit").click()

time.sleep(2)
driver.find_element("name", "form_submit").click()
time.sleep(8)

sendDungeonAttacks()

driver.find_element("id","item-provinces").click()
time.sleep(1)
driver.find_element("xpath",'//*[@class="ui-location ui-vassals"]').click()
time.sleep(1)
driver.find_element("xpath",'//*[@value="Събиране от всички"]').click()

time.sleep(5)
driver.quit()