from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random
#for x in range(10):
#  print random.randint(1,101)

url = 'https://docs.google.com/forms/d/e/1FAIpQLSeoDw8ZlbmhyxLAoI17iQuTIvCq2A8hBz27gmgvtWtl42s4Vg/viewform?vc=0&c=0&w=1'

age = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[1]'

age1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[2]/label/div/div[1]'
age2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[3]/label/div/div[1]'
age3 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[4]/label/div/div[1]'

gender1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/content/div/div[1]/label/div/div[1]'
gender2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/content/div/div[2]/label/div/div[1]'

mar1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[1]/label/div/div[1]'
mar2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[2]/label/div/div[1]'

ma1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/div[1]/label/div/div[1]'
ma2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/div[2]/label/div/div[1]'

answer1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/content/div/div[1]/label/div/div[1]'
answer2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/content/div/div[2]/label/div/div[1]'
answer3 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/content/div/div[3]/label/div/div[1]'
answer4 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/content/div/div[4]/label/div/div[1]'

submit = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div'

driver = webdriver.Edge()

for i in range (0, 50):
    driver.get(url)

    time.sleep(1.5)


    rand = random.randint(1,101)
    if (rand <= 50):
        checkbox = driver.find_element_by_xpath(age1)
    elif (rand <= 65):
        checkbox = driver.find_element_by_xpath(age2)
    else:
        checkbox = driver.find_element_by_xpath(age3)
    checkbox.click()
    time.sleep(0.5)

    if (random.randint(1,101) <= 50):
        checkbox = driver.find_element_by_xpath(gender1)
    else:
        checkbox = driver.find_element_by_xpath(gender2)
    checkbox.click()
    time.sleep(0.5)

    r = random.randint(1,101)
    if (r <= 50):
        checkbox = driver.find_element_by_xpath(mar1)
    else:
        checkbox = driver.find_element_by_xpath(mar2)
    checkbox.click()
    time.sleep(0.5)

    r = random.randint(1,101)
    if (r <= 50):
        checkbox = driver.find_element_by_xpath(ma1)
    else:
        checkbox = driver.find_element_by_xpath(ma2)
    checkbox.click()
    time.sleep(0.5)

    r = random.randint(1,101)
    if (r <= 25):
        checkbox = driver.find_element_by_xpath(answer1)
    elif (r <= 50):
        checkbox = driver.find_element_by_xpath(answer2)
    elif (r <= 75):
        checkbox = driver.find_element_by_xpath(answer3)
    else:
        checkbox = driver.find_element_by_xpath(answer4)
    checkbox.click()
    time.sleep(0.5)

    checkbox = driver.find_element_by_xpath(submit)
    checkbox.click()
    time.sleep(1)
    print(i)
