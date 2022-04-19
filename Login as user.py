from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")

driver.find_element(By.NAME, "username").send_keys("vinaywxyz")
driver.find_element(By.NAME, "password").send_keys("vinay0123")

driver.find_element(By.ID, "signin").click()




#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# serv_obj = Service("C:\webdrivers\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# driver.maximize_window()
#
# driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
# driver.find_element(By.NAME, "username").send_keys("vinaywxyz")
# driver.find_element(By.NAME, "password").send_keys("vinay012")
#
# driver.find_element(By.ID, "signin").click()

