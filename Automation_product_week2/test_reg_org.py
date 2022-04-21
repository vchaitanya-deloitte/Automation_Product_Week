from selenium import webdriver                                      #Registration of organizer
from selenium.webdriver.chrome.service import Service               #with same password and confirm
from selenium.webdriver.common.by import By                         #password
import pytest
import time

serv_obj = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("parvesharma")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("12345@django")

driver.find_element(By.ID, "signin").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text()='Register Organizer']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#id_username").send_keys("vinaychaitanyanr12345")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay1234567890")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay1234567890")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@type='submit']").click()


#
#
# serv_obj = Service("C:\webdrivers\chromedriver.exe")                        #Unable to register an organizer
# driver = webdriver.Chrome(service=serv_obj)                                 #using different password and confirm
# driver.maximize_window()                                                    #password
#
# driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
# time.sleep(3)
# driver.find_element(By.NAME, "username").send_keys("parvesharma")
# time.sleep(2)
# driver.find_element(By.NAME, "password").send_keys("12345@django")
#
# driver.find_element(By.ID, "signin").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//div[text()='Register Organizer']").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_username").send_keys("vinaychaitanyanr123")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay1234567")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay12345678")
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

