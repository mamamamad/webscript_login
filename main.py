from selenium import webdriver
import time


class Login:
    """ This class is for managing the entire login and logout process """
    def __init__(self) -> None:
        self.password = 0
        self.username= 0

    def log_in(self):
        # login with selenium 
        driver = webdriver.Chrome()
        driver.get('https://internet.birjand.ac.ir/login')
        driver.find_element('id',"username").send_keys(self.username)
        driver.find_element('id',"password").send_keys(self.password)
        driver.find_element("css selector", ".loginButton").click()
        driver.quit()
    def get_passuser(self):
        self.username = input("please enter Username: ")
        self.password = input("please enter Password: ")
    def save_file(self):
        # This function is for saving information in the file.
        file = open("C:\Program Files\logis_bir\up.txt",'w') 
        file.write(self.password)
        file.write(self.username)  
        file.write('a')  
        file.write('b')  
        file.close()
          


l= Login

l.save_file()






