from selenium import webdriver
import time
import os
import re

class Login:
    """ This class is for managing the entire login and logout process """
    def __init__(self) -> None:
        self.password = ''
        self.username= ''
        self.time = 60

    def log_in(self):
        # login with selenium 
        driver = webdriver.Chrome()
        driver.get('https://internet.birjand.ac.ir/login')
        driver.find_element('id',"username").send_keys(self.username)
        driver.find_element('id',"password").send_keys(self.password)
        driver.find_element("css selector", ".loginButton").click()
        print("login")
        time.sleep(1)

        driver.quit()
        exit()
    def get_passuser(self):
        # This function is used to receive the username and password. 
        while 1:
            self.username = input("please enter Username: ")
            self.password = input("please enter Password: ")
            
            save = input("save? N/Y")
            if save.lower() == 'n':
                pass
            elif save.lower() == 'y':
                print("pass saved")
                time.sleep(1)
                break 
        
        
    def save_file(self):
        # This function is for saving information in the file.
        file = open('Up.txt','w') 
        file.write(self.password)
        file.write('\n')
        file.write(self.username)   
        file.close()
    def check_network(self):
        # This function is for checking the internet status.
        t = self.time/5
        tag = 0
        while t:
            command = 'netsh wlan show interfaces'
            result = os.popen(command).read()
            ssid_pattern = r'SSID\s+:\s+(.*)'
            ssid_match = re.search(ssid_pattern, result)
            # find name wifi.
            if ssid_match.group(1) == "SARV I" or ssid_match.group(1) == "SARV2" or ssid_match.group(1) == "SARV4" or ssid_match.group(1) == "SARV3"or ssid_match.group(1) == "Network":
                tag = 1
                break
            else:
                t-=1
                time.sleep(5)
                if t == 0:
                    qu = input("The desired Wi-Fi network was not found. Are you still waiting? Y/N")
                    if qu.lower() == 'n':
                        pass
                    elif qu.lower() == 'y':
                        t = self.time/5
                else:
                    pass
        
        if tag == 0:
            exit()
        else:
            pass
    def read_file(self):
        # this file is used for read file.
        
        
        
        try:
            file = open('Up.txt','r')
            if file == None:
                self.get_passuser()
                self.save_file()
            else:    
                self.password,self.username  = file.readlines()   
                self.password = self.password.replace('\n','')
        except:
            self.get_passuser()
            self.save_file()
            
    def main(self):
        self.check_network()
        self.read_file()
        self.log_in()    
            

l= Login()
l.main()






