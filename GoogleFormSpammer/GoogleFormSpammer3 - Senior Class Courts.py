from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random
#for x in range(10):
#  print random.randint(1,101)

url = 'https://docs.google.com/forms/d/e/1FAIpQLScvBhTv80A8IL8bajmIBs0ooBTFNJoFLl4Ca7HZanCpGhZkXw/viewform'
b = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div/content/div/div[1]/label/div/div[1]'
submit = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div[1]/div'

driver = webdriver.Edge()

time.sleep(1)

for i in range (0, 500):
    driver.get(url)
    time.sleep(1)

    checkbox = driver.find_element_by_xpath(b)
    checkbox.click()
    time.sleep(1.5)

    checkbox = driver.find_element_by_xpath(submit)
    checkbox.click()
    time.sleep(1.5)



#
# b1 = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div'
# name1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]'
# name2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]'
#         #//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[4]
# contact1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input'
# next1 = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div[2]'
#
# driver = webdriver.Edge()
# time.sleep(1)
# driver.get(url)
# time.sleep(1)
#
# checkbox = driver.find_element_by_xpath(b1)
# checkbox.click()
# time.sleep(1.5)
#
# checkbox = driver.find_element_by_xpath(name1)
# checkbox.click()
# time.sleep(1.5)
#
# checkbox = driver.find_element_by_xpath(name2)
# checkbox.click()
# time.sleep(1.5)
#
# checkbox = driver.find_element_by_xpath(contact1)
# checkbox.send_keys("N/A")
# checkbox.click()
# time.sleep(1.5)
