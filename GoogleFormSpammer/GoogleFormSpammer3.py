from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random
#for x in range(10):
#  print random.randint(1,101)

url = 'https://docs.google.com/forms/d/e/1FAIpQLSd6JgpRcR-D6XcNx34EnN_pCVNUjmyhZkgEJlFNnp0PSoml6g/viewform?vc=0&c=0&w=1'

t1 = ''
t2 = ''
t3 = ''
t4 = ''

t5 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div[1]/div[2]/textarea'
t6 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]'
t7 = ''
t8 = ''

submit = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div'

driver = webdriver.Edge()

for i in range (0, 50):
    driver.get(url)

    time.sleep(1.5)

    # checkbox = driver.find_element_by_xpath(t1)
    # checkbox.click()
    # time.sleep(0.5)
    #
    # checkbox = driver.find_element_by_xpath(t2)
    # checkbox.click()
    # time.sleep(0.5)
    #
    # checkbox = driver.find_element_by_xpath(t3)
    # checkbox.click()
    # time.sleep(0.5)
    #
    # checkbox = driver.find_element_by_xpath(t4)
    # checkbox.click()
    # time.sleep(0.5)

    checkbox = driver.find_element_by_xpath(t6)
    driver.SendKeys("Teachout is Awsome!")

    checkbox = driver.find_element_by_xpath(submit)
    checkbox.click()
    time.sleep(1)
    print(i)
