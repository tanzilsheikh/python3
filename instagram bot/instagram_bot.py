#feel free to change randint parameters if you can 
#the bot is programed to be slow


from selenium import webdriver #this module is not installed by default
from time import sleep #to make this bot less bot like
from getpass import getpass #privacy 
from random import randint #to make this bot less bot like
import os
def login(): 
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    #This will type in the password 
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    # This will type in the password you provide
    sleep(1)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
    # This will click the login button
 
def likeandfollow():
    sleep(3)
    for h in hashtags:
        sleep(4)
        browser.get('https://www.instagram.com/explore/tags/'+h+'/')
        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
        #opens most recent post
        for i in range(count):
            sleep(randint(8,12))
            try:
                browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                #likes the post
                sleep(randint(5,13))
                browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                #follows the user
                sleep(randint(4,13))
                browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                #nest post
            except: #for unecpected pop-up(already following)
                browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]').click()
                #cancel 
                sleep(randint(4,13))
                browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
        sleep(randint(10,20))
        
username = input('Your username: ') #This will ask for your username
password = getpass('Your password.(won\'t display ): ') #This will ask for your password without displaying it on your screen
hashtags = input('hashtags(use spaces): ').split() #hash tags to search
count    = int(input("no of post for each hashtag: ")) 
browser = webdriver.Chrome(os.getcwd()+'/chromedriver.exe') #This will be the path to chromedriver.exe file 
browser.get("https://www.instagram.com/accounts/login/") #This will take you to the login page
sleep(randint(2,6)) 
login() 
sleep(randint(4,10)) 
likeandfollow()

##      warning!!! instagram has got really good and indentifying bots      ##






