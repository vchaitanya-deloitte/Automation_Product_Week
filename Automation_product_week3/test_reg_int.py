from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

serv_obj = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")

driver.find_element(By.NAME, "username").send_keys("parvesharma")
driver.find_element(By.NAME, "password").send_keys("12345@django")

driver.find_element(By.ID, "signin").click()

driver.find_element(By.XPATH, "//div[text()='Register Interest']").click()
driver.find_element(By.NAME, "name").send_keys("Football")
driver.find_element(By.NAME, "color").click()
driver.find_element(By.CSS_SELECTOR, "#content-wrapper > div > div.card-body.pagecontainer.regform > form > button").click()
