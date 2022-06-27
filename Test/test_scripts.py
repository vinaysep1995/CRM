from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:\\Users\\BB\\Downloads\\driver\\geckodriver.exe")
driver.get("https://collegevidya.edutra.io/login")
driver.maximize_window()

try:
    driver.find_element_by_css_selector("#email").send_keys("mis@blackboardindia.com")
    driver.find_element_by_css_selector("#password").send_keys("DES@123")
    driver.find_element_by_css_selector(".w-full.btn.btn-blue").click()
    driver.find_element_by_xpath("//header/div[1]/div[1]/button[1]/*[1]").click()
    driver.find_element_by_xpath("//span[@id='leads']").click()
    Emails = driver.find_elements_by_xpath("//div[@class='flex flex-col']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/p")
    #assert Emails == 'idmayank@gmail.com'
    for Email in Emails:
        if Email == "idmayank@gmail.com":
            print(Email.text)
            driver.find_element_by_xpath("//div[@class='flex flex-col']/div[1]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]").click()
            #driver.save_screenshot('screenshot.png')
            driver.find_element_by_xpath("//div[@class='flex flex-col']/div[1]/div[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/div[1]/a").click()
except NoSuchElementException:
   pass

