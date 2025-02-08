from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium import 
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.atom.com/name/Test")
time.sleep(20)
link = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/div[2]/a[2]')
link.click()
driver.quit()
