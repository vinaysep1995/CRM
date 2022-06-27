from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from ModuleObject.Lead import Lead


class LOGIN:

    def __init__(self, driver):
        self.driver = driver

    try:
        userid = (By.CSS_SELECTOR, "#email")
        password = (By.CSS_SELECTOR, "#password")
        signin = (By.CSS_SELECTOR, ".w-full.btn.btn-blue")

        def getUserId(self):
            return self.driver.find_element(*LOGIN.userid)

        def getPassword(self):
            return self.driver.find_element(*LOGIN.password)

        def getSignin(self):
            return self.driver.find_element(*LOGIN.signin)

        def Leads(self):
            lead = Lead(self.driver)
            return lead

    except NoSuchElementException:
        pass





