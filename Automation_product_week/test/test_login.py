# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
#
# def test_login_user():
#     serv_obj = Service("C:\webdrivers\chromedriver.exe")
#     driver = webdriver.Chrome(service=serv_obj)
#     driver.maximize_window()
#
#     driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#     driver.find_element(By.NAME, "username").send_keys("vinaychaitanyanr")
#     driver.find_element(By.NAME, "password").send_keys("vinay123")
#
#     driver.find_element(By.ID, "signin").click()
#
#     assert driver.current_url == "https://hashedinfunzone-urtjok3rza-wl.a.run.app/employee/"

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_login():
    serv_obj = Service("C:\webdrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()

    driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")

    driver.find_element(By.NAME, "username").send_keys("parvesharma")
    driver.find_element(By.NAME, "password").send_keys("Sh$560037KA")

    driver.find_element(By.ID, "signin").click()

    assert driver.current_url == "https://hashedinfunzone-urtjok3rza-wl.a.run.app/owner/"
