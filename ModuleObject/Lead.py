import pytest
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



class Lead:

    def __init__(self, driver):
        self.driver = driver
    try:
        dashboard = (By.XPATH, "//header/div[1]/div[1]/button[1]/*[1]")
        alllead = (By.XPATH, "//span[@id='leads']")
        addlead = (By.XPATH, "//header/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]")
        name = (By.XPATH, "//input[@id='full_name']")
        email = (By.XPATH, "//input[@id='email']")
        phone = (By.ID, "phone")
        dob = (By.ID,"dob")
        remark = (By.ID,"remark")
        source = (By.XPATH,"// select[ @ id = 'source']")
        subcource = (By.ID,"sub_source_id")
        stage = (By.ID,"stage")
        reason = (By.ID,"reason")
        sureason = (By.ID,"subreason")
        counsellor = (By.ID,"counsellor")
        institute = (By.ID,"institute")
        courses = (By.ID,"courses")
        #specialization = (By.ID,"specialization")
        states = (By.ID,"states")
        city = (By.ID,"city")
        add = (By.CSS_SELECTOR,".pt-5 div button")

        def getDashboard(self):
            return self.driver.find_element(*Lead.dashboard)

        def getAlllead(self):
            return self.driver.find_element(*Lead.alllead)

        def getAddlead(self):
            return self.driver.find_element(*Lead.addlead)

        def getName(self):
            return self.driver.find_element(*Lead.name)

        def getEmail(self):
            return self.driver.find_element(*Lead.email)

        def getPhone(self):
            return self.driver.find_element(*Lead.phone)

        def getDOB(self):
            return self.driver.find_element(*Lead.dob)

        def getRemark(self):
            return self.driver.find_element(*Lead.remark)

        def getSource(self):
            return self.driver.find_element(*Lead.source)

        def getSubsource(self):
            return self.driver.find_element(*Lead.subcource)

        def getStage(self):
            return self.driver.find_element(*Lead.stage)

        def getReason(self):
            return self.driver.find_element(*Lead.reason)

        def getSubreason(self):
            return self.driver.find_element(*Lead.sureason)

        def getCounsellor(self):
            return self.driver.find_element(Lead.counsellor)

        def getInstiture(self):
            return self.driver.find_element(*Lead.institute)

        def getCource(self):
            return self.driver.find_element(*Lead.courses)

        #def getSpecialization(self):
         #   return self.driver.find_element(*Lead.specialization)

        def getState(self):
            return self.driver.find_element(*Lead.states)

        def getCity(self):
            return self.driver.find_element(*Lead.city)

        def getAdd(self):
            return self.driver.find_element(*Lead.add)

    except NoSuchElementException:
        pass



