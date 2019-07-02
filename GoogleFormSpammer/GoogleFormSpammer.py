from selenium import webdriver
import time

url = 'https://docs.google.com/forms/d/1LaZf1hIPnfl8MCbv6M5oJ0P0DK-ice4qOe3kNACrPT4/viewform?vc=0&c=0&w=1&edit_requested=true'
xpathCheckbox0 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/label/div/div[1]'
xpathCheckbox1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div[6]/div/label/div/div[1]'
xpathCheckbox2 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div[7]/div/label/div/div[1]'
xpathSubmitButton = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div'
xpathSubmitAnotherResponce = '/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/a'

driver = webdriver.Edge()
driver.get(url)

for i in range (0, 500):
    checkbox = driver.find_element_by_xpath(xpathCheckbox0)
    checkbox.click()

    time.sleep(0.5)

    checkbox = driver.find_element_by_xpath(xpathCheckbox1)
    checkbox.click()

    time.sleep(0.5)

    checkbox = driver.find_element_by_xpath(xpathCheckbox2)
    checkbox.click()

    time.sleep(0.5)

    button = driver.find_element_by_xpath(xpathSubmitButton)
    button.click()

    time.sleep(1)

    button = driver.find_element_by_xpath(xpathSubmitAnotherResponce)
    button.click()

    time.sleep(1)
