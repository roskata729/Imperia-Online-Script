import getpass
import time

def getUsernameFromInput():
    return input("Enter your username: ")

def getPasswordFromInput():
    return getpass.getpass("Enter your password: ")

def loginToImperiaOnlineWithGivenCredentials(driver, username, password):
    driver.get("https://www122.imperiaonline.org/")

    time.sleep(2)
    # # find username/email field and send the username itself to the input field
    driver.find_element("id", "login-user").send_keys(username)
    driver.find_element("id", "login-pass").send_keys(password)
    driver.find_element("name", "image-submit").click()

    time.sleep(2)
    driver.find_element("name", "form_submit").click()
    time.sleep(8)
