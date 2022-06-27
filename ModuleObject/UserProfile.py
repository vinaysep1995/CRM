import pytest
import inspect
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class UserProfile:

    def __init__(self, driver):
        self.driver = driver
    try:

        profile = (By.XPATH, "//header/div[1]/div[2]/div[3]/button[1]/img[1]")
        myprofile = (By.XPATH, "//p[contains(text(),'My Profile')]")

        def getProfile(self):
            return self.driver.find_element(*UserProfile.profile)

        def getMyProfile(self):
            return self.driver.find_element(*UserProfile.myprofile)

    except NoSuchElementException:
        pass





