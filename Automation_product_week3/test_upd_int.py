from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time
import unittest


class Test(unittest.TestCase):
    def test_upd_int(self):
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
        driver.find_element(By.XPATH, "//div[text()='Update Interests']").click()
        driver.find_element(By.ID, "id_interests_1").click()
        driver.find_element(By.CSS_SELECTOR,
                            "#content-wrapper > div > div.card-body.pagecontainer > form > div.pagebtngrp > button").click()
        upd = driver.current_url
        self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/employee/", upd, "Interest was not updated")
        time.sleep(5)
        print("Test cases executed successfully")

# class Test(unittest.TestCase):
#     def test_upd_int(self):
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.NAME, "username").send_keys("vinaychaitanyanr1")
#         time.sleep(2)
#         driver.find_element(By.NAME, "password").send_keys("vinay12345")
#         time.sleep(2)
#         driver.find_element(By.ID, "signin").click()
#         driver.find_element(By.XPATH, "//div[text()='Update Interests']").click()
#         driver.find_element(By.ID, "id_interests_1").click()
#         driver.find_element(By.CSS_SELECTOR,
#                             "#content-wrapper > div > div.card-body.pagecontainer > form > div.pagebtngrp > button").click()
#         upd = driver.current_url
#         self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/employee/", upd, "Interest was not updated")
#         time.sleep(5)
