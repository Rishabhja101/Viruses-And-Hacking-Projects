from selenium import webdriver
import time

url = 'https://docs.google.com/forms/d/1LaZf1hIPnfl8MCbv6M5oJ0P0DK-ice4qOe3kNACrPT4/viewform?vc=0&c=0&w=1&edit_requested=true'
xpathCheckbox = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/label/div/div[1]'
#xpathSubmitButton = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div/content/span'
xpathSubmitButton = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div'


driver = webdriver.Edge()
driver.get(url)

checkbox = driver.find_element_by_xpath(xpathCheckbox)
checkbox.click()

time.sleep(0.5)

button = driver.find_element_by_xpath(xpathSubmitButton)
button.click()
