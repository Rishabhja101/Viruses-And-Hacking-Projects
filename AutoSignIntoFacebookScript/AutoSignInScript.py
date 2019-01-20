from selenium import webdriver

username = '' # store username here
password = '' # store password here

url = 'https://www.facebook.com/'

driver = webdriver.Edge() # adjust for the default browser on the computer
driver.get(url)

username_box = driver.find_element_by_id('email')
username_box.send_keys(username)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)

login_button = driver.find_element_by_id('u_0_2')
login_button.submit()
