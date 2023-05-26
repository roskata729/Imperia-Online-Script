from selenium import webdriver

def closeLastLoginsTab(driver):
    if driver.find_element("xpath",'//[@class="txt-title"]'):     
        driver.find_element("xpath",'//[@title="Затваряне"]').click()