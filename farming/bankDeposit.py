import time

def collectBankDeposit(driver):
    driver.find_element("xpath",'//*[@title="Бързи бутони"]').click()
    time.sleep(1)
    driver.find_element("xpath",'//*[@title="Банка"]').click()
    time.sleep(2)
    driver.find_element("xpath",'//*[@class="ui-ib tab-2 active"]').click()

    countdownElement = driver.find_element("xpath",'//*[@class="countdown centered th-time"]')
    countdownValue = countdownElement.get_attribute("now")
    if countdownValue == 0 :
        driver.find_element("xpath",'//*[@value="Изтегляне"]').click()
    else:
        print("Не е приключил таймера на депозита.")