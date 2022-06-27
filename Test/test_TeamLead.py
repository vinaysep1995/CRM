from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


from ModuleObject.Lead import Lead
from ModuleObject.LOGIN import LOGIN
from utilities.BaseClass import BaseClass
from TestData.TestData import TestData
from ModuleObject.UserProfile import UserProfile


class TestOne(BaseClass):

    def test_LeadAddition(self,getData):

        log = self.getLogger()
        login = LOGIN(self.driver)
        lead = Lead(self.driver)
        lead = login.Leads()
        login.getUserId().send_keys(getData["userid"])
        login.getPassword().send_keys(getData["password"])
        login.getSignin().click()
        log.info("TeamLead login successfully")
        lead.getDashboard().click()
        lead.getAlllead().click()
        lead.getAddlead().click()
        self.driver.implicitly_wait(10)
        lead.getName().send_keys(getData["name"])
        lead.getEmail().send_keys(getData["email"])
        lead.getPhone().send_keys(getData["phone"])
        #lead.getDOB().send_keys(getData["dob"])
        datefield = self.driver.find_element_by_id('dob')
        datefield.click()
        datefield.send_keys("01012001")
        log.info("personal details added successfully")
        lead.getRemark().send_keys(getData["remark"])
        self.selectoptionByValue(lead.getSource(),getData["source"])
        self.selectoptionByValue(lead.getSubsource(),getData["subsource"])
        self.selectoptionByValue(lead.getStage(),getData["stage"])
        self.selectoptionByValue(lead.getReason(),getData["reason"])
        self.selectoptionByValue(lead.getSubreason(),getData["sureason"])
        counsellor = Select(self.driver.find_element_by_id("counsellor")).select_by_value('35')
        self.selectoptionByValue(lead.getInstiture(),getData["institute"])
        self.selectoptionByValue(lead.getCource(),getData['courses'])
        log.info("Academic detail added successfully")
        #self.selectoptionByValue(lead.getSpecialization(),getData["specialization"])
        self.selectoptionByValue(lead.getState(),getData["states"])
        self.selectoptionByValue(lead.getCity(),getData["city"])
        log.info("address detail added")
        lead.getAdd().click()
        log.info("lead added successfully")

    @pytest.fixture(params=TestData.test_TeamLead_LeadAddition)
    def getData(self, request):
        return request.param



