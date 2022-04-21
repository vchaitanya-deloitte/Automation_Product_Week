from selenium import webdriver  # Login with right credentials
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time
import unittest


class Test(unittest.TestCase):
    def test_login(self):
        serv_obj = Service("C:\webdrivers\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        time.sleep(2)

        driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")

        driver.find_element(By.NAME, "username").send_keys("vinaychaitanyanr")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("vinay12345")
        time.sleep(2)
        driver.find_element(By.ID, "signin").click()
        time.sleep(2)
        exp_text = 'Hi, vinaychaitanyanr'
        act_text = driver.find_element_by_xpath("//h3[text()='Hi, vinaychaitanyanr']").text
        self.assertEqual(act_text, exp_text, "Error message not shown")
        time.sleep(5)
        print("Test case passed successfully")
# 
#
# class Test(unittest.TestCase):  # Unable to login with right
#     def test_login(self):  # username and wrong password
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.NAME, "username").send_keys("vinaychaitanyanr")
#         time.sleep(2)
#         driver.find_element(By.NAME, "password").send_keys("vinay123456")
#         time.sleep(2)
#         driver.find_element(By.ID, "signin").click()
#         time.sleep(2)
#         exp_text = 'Hi, vinaychaitanyanr'
#         act_text = driver.find_element_by_xpath("//h3[text()='Hi, vinaychaitanyanr']").text
#         self.assertEqual(act_text, exp_text, "Error message not shown")
#         time.sleep(5)
#
#
# class Test(unittest.TestCase):  # Unable to login with right
#     def test_login(self):  # password and wrong username
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.NAME, "username").send_keys("vinaychaitanyanr")
#         time.sleep(2)
#         driver.find_element(By.NAME, "password").send_keys("vinay123456")
#         time.sleep(2)
#         driver.find_element(By.ID, "signin").click()
#         time.sleep(2)
#         exp_text = 'Hi, vinaychaitanyanr'
#         act_text = driver.find_element_by_xpath("//h3[text()='Hi, vinaychaitanyanr']").text
#         self.assertEqual(act_text, exp_text, "Error message not shown")
#         time.sleep(5)



# class Test(unittest.TestCase):  # Unable to login with right
#     def test_login(self):  # password and wrong username
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.NAME, "username").send_keys("vinaychaitan")
#         time.sleep(2)
#         driver.find_element(By.NAME, "password").send_keys("vinay12345")
#         time.sleep(2)
#         driver.find_element(By.ID, "signin").click()
#         time.sleep(2)
#         exp_text = 'Hi, vinaychaitanyanr'
#         act_text = driver.find_element_by_xpath("//h3[text()='Hi, vinaychaitanyanr']").text
#         self.assertEqual(act_text, exp_text, "Error message not shown")
#         time.sleep(5)
