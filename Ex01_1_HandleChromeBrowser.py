import unittest
from selenium import webdriver
import time
class MyTestCase(unittest.TestCase):
    def test_launch_browser(self):
      filepath="C:\\Users\\UVANDAVA\\PycharmProjects\\SelinumPythonproject\\driver\\chromedriver.exe"
      driver=webdriver.Chrome(filepath)
      time.sleep(1)
      driver.quit()

if __name__ == '__main__':
    unittest.main()
