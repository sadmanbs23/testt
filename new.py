import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.aiub.edu/")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/ul/li[1]/a/span").click()

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[1]/input").send_keys("15-30771-3")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[2]/input[1]").send_keys("59050597")

time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[4]/button").click()
