from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://gaana.com/")
sleep(2)
driver.maximize_window()
sleep(8)
driver.find_element_by_class_name("popup-close")\
    .click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/a")\
    .click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[3]/div[2]/div[5]/div/h2/a[2]")\
    .click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[3]/div[2]/div[4]/div[1]/div[2]/div/div/div/p[3]/a")\
    .click()
