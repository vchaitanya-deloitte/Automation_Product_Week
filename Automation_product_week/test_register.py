from selenium import webdriver  # Register with different number
from selenium.webdriver.chrome.service import Service  # of interests using appropriate
from selenium.webdriver.common.by import By  # username and password
import pytest
import time
import unittest


class Test(unittest.TestCase):
    def test_register(self):
        serv_obj = Service("C:\webdrivers\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        time.sleep(2)
        driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")

        driver.find_element(By.CSS_SELECTOR,
                            "body > div > form > center > a").click()
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("vinayabcdefgh")
        time.sleep(5)
        driver.find_element(By.NAME, "password1").send_keys("vinay0123456789")
        driver.find_element(By.NAME, "password2").send_keys("vinay0123456789")
        time.sleep(5)
        driver.find_element(By.ID, "id_interests_0").click()
        driver.find_element(By.ID, "id_interests_1").click()
        # driver.find_element(By.ID, "id_interests_2").click()
        # driver.find_element(By.ID, "id_interests_3").click()
        # driver.find_element(By.ID, "id_interests_4").click()
        time.sleep(5)
        driver.find_element(By.ID, "signup").click()
        time.sleep(2)
        reg = driver.current_url
        self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/login_form/", reg, "Registration was unsuccessful")
        time.sleep(5)
        print("Test case passed successfully")

# class Test(unittest.TestCase):
#     def test_register(self):
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.CSS_SELECTOR,
#                             "body > div > form > center > a").click()
#         time.sleep(2)
#         driver.find_element(By.NAME, "username").send_keys("vinayabcd")
#         time.sleep(5)
#         driver.find_element(By.NAME, "password1").send_keys("vinay0123456")
#         driver.find_element(By.NAME, "password2").send_keys("vinay0123456")
#         time.sleep(5)
#         driver.find_element(By.ID, "id_interests_0").click()
#         driver.find_element(By.ID, "id_interests_1").click()
#         driver.find_element(By.ID, "id_interests_2").click()
#         driver.find_element(By.ID, "id_interests_3").click()
#         time.sleep(5)
#         driver.find_element(By.ID, "signup").click()
#         time.sleep()
#         reg = driver.current_url
#         self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/", reg, "Registration was unsuccessful")
#         time.sleep(5)
#
#
# class Test(unittest.TestCase):
#     def test_register(self):
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.CSS_SELECTOR,
#                             "body > div > form > center > a").click()
#         time.sleep(2)
#         driver.find_element(By.NAME, "username").send_keys("vinayabcd")
#         time.sleep(5)
#         driver.find_element(By.NAME, "password1").send_keys("vinay0123456")
#         driver.find_element(By.NAME, "password2").send_keys("vinay0123456")
#         time.sleep(5)
#         driver.find_element(By.ID, "id_interests_0").click()
#         driver.find_element(By.ID, "id_interests_1").click()
#         driver.find_element(By.ID, "id_interests_2").click()
#         time.sleep(5)
#         driver.find_element(By.ID, "signup").click()
#         time.sleep()
#         reg = driver.current_url
#         self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/", reg, "Registration was unsuccessful")
#         time.sleep(5)
#
#
# class Test(unittest.TestCase):
#     def test_register(self):
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.CSS_SELECTOR,
#                             "body > div > form > center > a").click()
#         time.sleep(2)
#         driver.find_element(By.NAME, "username").send_keys("vinayabcd")
#         time.sleep(5)
#         driver.find_element(By.NAME, "password1").send_keys("vinay0123456")
#         driver.find_element(By.NAME, "password2").send_keys("vinay0123456")
#         time.sleep(5)
#         driver.find_element(By.ID, "id_interests_0").click()
#         driver.find_element(By.ID, "id_interests_1").click()
#         time.sleep(5)
#         driver.find_element(By.ID, "signup").click()
#         time.sleep()
#         reg = driver.current_url
#         self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/", reg, "Registration was unsuccessful")
#         time.sleep(5)
#
#
# class Test(unittest.TestCase):
#     def test_register(self):
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.CSS_SELECTOR,
#                             "body > div > form > center > a").click()
#         time.sleep(2)
#         driver.find_element(By.NAME, "username").send_keys("vinayabcd")
#         time.sleep(5)
#         driver.find_element(By.NAME, "password1").send_keys("vinay0123456")
#         driver.find_element(By.NAME, "password2").send_keys("vinay0123456")
#         time.sleep(5)
#         driver.find_element(By.ID, "id_interests_0").click()
#         time.sleep(5)
#         driver.find_element(By.ID, "signup").click()
#         time.sleep()
#         reg = driver.current_url
#         self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/", reg, "Registration was unsuccessful")
#         time.sleep(5)
#
#
# class Test(unittest.TestCase):  # unable to register using
#     def test_register(self):  # different password and
#         serv_obj = Service("C:\webdrivers\chromedriver.exe")  # confirm password
#         driver = webdriver.Chrome(service=serv_obj)
#         driver.maximize_window()
#         time.sleep(2)
#         driver.get("https://hashedinfunzone-urtjok3rza-wl.a.run.app/")
#
#         driver.find_element(By.CSS_SELECTOR,
#                             "body > div > form > center > a").click()
#         time.sleep(2)
#         driver.find_element(By.NAME, "username").send_keys("vinayabcd")
#         time.sleep(5)
#         driver.find_element(By.NAME, "password1").send_keys("vinay0123456")
#         driver.find_element(By.NAME, "password2").send_keys("vinay012345")
#         time.sleep(5)
#         driver.find_element(By.ID, "id_interests_0").click()
#         driver.find_element(By.ID, "id_interests_1").click()
#         driver.find_element(By.ID, "id_interests_2").click()
#         driver.find_element(By.ID, "id_interests_3").click()
#         driver.find_element(By.ID, "id_interests_4").click()
#         time.sleep(5)
#         driver.find_element(By.ID, "signup").click()
#         time.sleep()
#         reg = driver.current_url
#         self.assertEqual("https://hashedinfunzone-urtjok3rza-wl.a.run.app/", reg, "Registration was unsuccessful")
#         time.sleep(5)
