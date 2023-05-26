from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

def sendDungeonAttacks(driver):
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
                time.sleep(3)
                #driver.find_element("xpath",'//*[@class="flanks-flank-archers"]')
                #driver.find_element("id", "attack-general").click()
                # time.sleep(2)
                driver.find_element("id", "select-all-army").click()
                time.sleep(2)
                sendAttackButton = driver.find_element("xpath", "//button[text()='Полева битка']") or driver.find_element("xpath", "//button[text()='Крепостна Обсада']")
                print(sendAttackButton)
                sendAttackButton.click()
    except NoSuchElementException:
        print("В момента няма налични безплатни атаки")

    time.sleep(5)