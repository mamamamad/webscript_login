from selenium import webdriver



import time


username = "4001226047"
password = "5720157913"


driver = webdriver.Chrome()

driver.get('https://internet.birjand.ac.ir/login')


driver.find_element('id',"username").send_keys(username)

driver.find_element('id',"password").send_keys(password)



driver.find_element("css selector", ".loginButton").click()

driver.quit()








