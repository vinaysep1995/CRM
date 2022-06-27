import pytest
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from ModuleObject.LOGIN import SignIn


class LeadStaging:

    def __init__(self):
        self.driver = driver

    alllead = (By.XPATH,"//span[@id='leads']")
    searchlead =(By.CSS_SELECTOR,".mb-4")

    def Credentials(self):
        usercredentials = UserCredentials(self.driver)
        return usercredentials

    def getAllLead(self):
        return self.driver.find_element(*LeadStaging.alllead)

    def getSearchLead(self):
        return self.driver.find_element(*LeadStaging.searchlead)








