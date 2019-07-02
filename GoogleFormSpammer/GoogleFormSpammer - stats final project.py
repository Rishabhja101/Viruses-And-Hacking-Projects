from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random
#for x in range(10):
#  print random.randint(1,101)

url = 'https://forms.gle/UYgsgJCfeZNu58jx9'

t1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[1]/label/div/div[1]'
t2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[2]/label/div/div[1]'
t3 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[3]/label/div/div[1]'
t4 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[4]/label/div/div[1]'
t5 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[5]/label/div/div[1]'
t6 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[6]/label/div/div[1]'
t7 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[7]/label/div/div[1]'
t8 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[8]/label/div/div[1]'
t9 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[9]/label/div/div[1]'
t10 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[10]/label/div/div[1]'
t11 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/span/div/div[11]/label/div/div[1]'


submit = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div'

driver = webdriver.Edge()

for i in range (0, 18):
    driver.get(url)

    time.sleep(1.5)

    rand = random.randint(1,101)
    if (rand <= 2):
        checkbox = driver.find_element_by_xpath(t1)
    elif (rand <= 3):
        checkbox = driver.find_element_by_xpath(t2)
    elif (rand <= 6):
        checkbox = driver.find_element_by_xpath(t3)
    elif (rand <= 10):
        checkbox = driver.find_element_by_xpath(t4)
    elif (rand <= 15):
        checkbox = driver.find_element_by_xpath(t5)
    elif (rand <= 25):
        checkbox = driver.find_element_by_xpath(t6)
    elif (rand <= 40):
        checkbox = driver.find_element_by_xpath(t7)
    elif (rand <= 60):
        checkbox = driver.find_element_by_xpath(t8)
    elif (rand <= 85):
        checkbox = driver.find_element_by_xpath(t9)
    elif (rand <= 95):
        checkbox = driver.find_element_by_xpath(t10)
    else:
        checkbox = driver.find_element_by_xpath(t11)
    checkbox.click()
    time.sleep(0.5)

    checkbox = driver.find_element_by_xpath(submit)
    checkbox.click()
    time.sleep(1)
    print(i)
