import time

def collectVassalGold(driver):
    driver.find_element("id","item-provinces").click()
    time.sleep(1)
    driver.find_element("xpath",'//*[@class="ui-location ui-vassals"]').click()
    time.sleep(1)
    driver.find_element("xpath",'//*[@value="Събиране от всички"]').click()