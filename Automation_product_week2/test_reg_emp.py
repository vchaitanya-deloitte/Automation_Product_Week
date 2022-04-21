from selenium import webdriver  # registration of employee by selection different number
from selenium.webdriver.chrome.service import Service  # of interests
from selenium.webdriver.common.by import By
import pytest
import time

serv_obj = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")

driver.find_element(By.NAME, "username").send_keys("parvesharma")
time.sleep(3)
driver.find_element(By.NAME, "password").send_keys("12345@django")

driver.find_element(By.ID, "signin").click()

driver.find_element(By.XPATH, "//div[text()='Register Employee']").click()
driver.find_element(By.NAME, "username").send_keys("vinaychaitanya")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay123456")
driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay123456")

driver.find_element(By.ID, "id_interests_0").click()
driver.find_element(By.ID, "id_interests_1").click()
driver.find_element(By.ID, "id_interests_2").click()
driver.find_element(By.ID, "id_interests_3").click()
driver.find_element(By.ID, "id_interests_4").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# serv_obj = Service("C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.maximize_window()
#
# driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
# driver.find_element(By.NAME, "username").send_keys("parvesharma")
# time.sleep(3)
# driver.find_element(By.NAME, "password").send_keys("12345@django")
#
# driver.find_element(By.ID, "signin").click()
#
# driver.find_element(By.XPATH, "//div[text()='Register Employee']").click()
# driver.find_element(By.NAME, "username").send_keys("vinaychaitanya")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay123456")
# driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay123456")
#
# driver.find_element(By.ID, "id_interests_0").click()
# driver.find_element(By.ID, "id_interests_1").click()
# driver.find_element(By.ID, "id_interests_2").click()
# driver.find_element(By.ID, "id_interests_3").click()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# serv_obj = Service("C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.maximize_window()
#
# driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
# driver.find_element(By.NAME, "username").send_keys("parvesharma")
# time.sleep(3)
# driver.find_element(By.NAME, "password").send_keys("12345@django")
#
# driver.find_element(By.ID, "signin").click()
#
# driver.find_element(By.XPATH, "//div[text()='Register Employee']").click()
# driver.find_element(By.NAME, "username").send_keys("vinaychaitanya")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay123456")
# driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay123456")
#
# driver.find_element(By.ID, "id_interests_0").click()
# driver.find_element(By.ID, "id_interests_1").click()
# driver.find_element(By.ID, "id_interests_2").click()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# serv_obj = Service("C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.maximize_window()
#
# driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
# driver.find_element(By.NAME, "username").send_keys("parvesharma")
# time.sleep(3)
# driver.find_element(By.NAME, "password").send_keys("12345@django")
#
# driver.find_element(By.ID, "signin").click()
#
# driver.find_element(By.XPATH, "//div[text()='Register Employee']").click()
# driver.find_element(By.NAME, "username").send_keys("vinaychaitanya")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay123456")
# driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay123456")
#
# driver.find_element(By.ID, "id_interests_0").click()
# driver.find_element(By.ID, "id_interests_1").click()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# serv_obj = Service("C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.maximize_window()
#
# driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
# driver.find_element(By.NAME, "username").send_keys("parvesharma")
# time.sleep(3)
# driver.find_element(By.NAME, "password").send_keys("12345@django")
#
# driver.find_element(By.ID, "signin").click()
#
# driver.find_element(By.XPATH, "//div[text()='Register Employee']").click()
# driver.find_element(By.NAME, "username").send_keys("vinaychaitanya")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#id_password1").send_keys("vinay123456")
# driver.find_element(By.CSS_SELECTOR, "#id_password2").send_keys("vinay123456")
#
# driver.find_element(By.ID, "id_interests_0").click()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
