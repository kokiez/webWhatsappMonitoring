from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageEnhance, ImageFilter
import PIL
import time
import sys
import datetime
import os.path
from selenium.webdriver.common.by import By
import webserver


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=chrome_options)

copyname="span[title='online']"
copysearch = "div[title='Search input textbox']"
website = "https://web.whatsapp.com/"
browser.get(website)
time.sleep(3)

webserver.keep_alive()
time.sleep(3)
print("")
print("")
name = input("Enter Number of contact: ")


img_phone = '/html/body/div[1]/div/div/div[4]/div/div/div[1]'
WebDriverWait(browser, 500).until(ec.presence_of_element_located((By.XPATH, img_phone)))

#----------------------------------------------------------------
WebDriverWait(browser, 500).until(ec.presence_of_element_located((By.CSS_SELECTOR,"span[data-testid='chat']")))
time.sleep(2)
newchat = browser.find_element(By.CSS_SELECTOR,"span[data-testid='chat']")
newchat.click()
time.sleep(2)

def searchNum(browser, name):
    WebDriverWait(browser, 500).until(ec.presence_of_element_located((By.CSS_SELECTOR, copysearch)))
    search = browser.find_element(By.CSS_SELECTOR, copysearch)
    search.click()
    search.clear()
    search.send_keys(name)
    time.sleep(1)

# A beautiful while loop for quality of service. so incase the number is searched and results were not expected, user will have chance to search again. 
searchSuccess = False
while searchSuccess == False:
    try:
        WebDriverWait(browser, 500).until(ec.presence_of_element_located((By.CLASS_NAME, "zoWT4")))
        contacts = browser.find_elements(By.CLASS_NAME, "zoWT4")
        tempCount = 0
        for a in contacts:
            print(str(tempCount)+") "+a.text)
            tempCount+=1
        print("")    
        print("The Above contacts were found after searching")
        print("From the above contacts, Select an option from 0 to "+str(len(contacts)))
        print("If you wish to 'Search for New Number', Enter new number")
        print("If you want to end this program, press 'CTRL + C' Keys")
        choice = input()
        print("")
        time.sleep(3)
        nameOfContact = contacts[int(choice)].text
        try:
            contacts[int(choice)].click()
            searchSuccess = True
        except:
            searchNum(browser, choice)
            
    except:
        try:
            ## no contacts found
            element = browser.find_element(By.CSS_SELECTOR, "span[class='i0jNr']")
            print(element.text)
            print("Do you wish to search for a new Number? \nIf 'YES', Enter new number. \nIf 'NO', press 'CTRL + C' to end Program. ")
            name  = input()
            print("")
            searchNum(browser, name)
        except:
            aa = "nothing"
#----------------------------------------------------------------    
print("")
print("")
print("")
print("")
print("Web Whatsapp Monitoring Started")

online_time=0 
tempFile = "temp"
if (not os.path.exists(tempFile + "_history.txt")):
    f = open(tempFile + "_history.txt", "a+")
    f.close()
time.sleep(2) 
if (not os.path.exists(tempFile + "_log.txt")):
    f = open(tempFile + "_log.txt", "a+")
    f.close()
time.sleep(2) 

while True:

    try:
        lastseen = browser.find_element(By.CSS_SELECTOR, copyname)
        lastseen=lastseen.text
        if lastseen == "typing..." or lastseen == "online":
            first_time = datetime.datetime.now()
            firsttime=str(first_time)
            f = open(tempFile + "_log.txt","a+")

            print(firsttime[ 0 : 19 ], end=" ")
            f.write(firsttime[ 0 : 19 ])

            print(" - ONLINE")
            f.write(" - ONLINE")

            f.write("\n\n")
            f.close()
            try:
                lastseen = browser.find_element(By.CSS_SELECTOR, copyname)
                lastseen=lastseen.text
                while lastseen == "typing..." or lastseen == "online":
                    try:
                        lastseen = browser.find_element(By.CSS_SELECTOR, copyname)
                        lastseen=lastseen.text
                    except:
                        lastseen = "."

            except:        
                print("no last seen!")


            later_time = datetime.datetime.now()
            latertime=str(later_time)
            f = open(tempFile + "_log.txt","a+")

            print(latertime[ 0 : 19 ], end=" ")
            f.write(latertime[ 0 : 19 ])

            print(" - OFFLINE")
            f.write(" - OFFLINE")
            f.write("\n\n")
            f.close()
      
            difference = later_time - first_time
            datetime.timedelta(0, 8, 562000)
            seconds_in_day = 24 * 60 * 60
            online_time = divmod(difference.days * seconds_in_day + difference.seconds, 60)

            f = open(tempFile + "_history.txt", "a+")

            print(tempFile,end=" ")
            f.write(tempFile)

            print(" was online for duration ",end=" ")
            f.write(" was online for duration ")

            print(str(online_time),end=" ")
            f.write(str(online_time))

            print(" on date ",end=" ")
            f.write(" on date ")

            print(firsttime[ 0 : 19 ])
            f.write(firsttime[ 0 : 19 ])
            f.write("\n\n")
            f.close()
    except:
        try:
            browser.find_element(By.CSS_SELECTOR, "div[title='loading messages…']")
            #----------------------------------------------------------------
            newchat = browser.find_element(By.CSS_SELECTOR,"span[data-testid='chat']")
            newchat.click()
            time.sleep(2)
            search = browser.find_element(By.CSS_SELECTOR, copysearch)
            search.click()
            search.clear()
            search.send_keys(name)
            time.sleep(1)
            user = browser.find_element(By.CSS_SELECTOR, "span[title='"+nameOfContact+"']")
            time.sleep(3)
            user.click()
            #---------------------------------------------------------------- 
        except:
            aa = "nothing"




