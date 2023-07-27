from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'

def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)


  

def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        
        
print ("[-[ TH3 T00L IS CR34T3D BY F9IISU ]-]")

emailx=str(input("➣Enter email : "))

pwx =str(input("➣Enter pswrd : "))

aclass()

msg4=str(input("➣Enter post link : "))

msg5=str(input("➣Enter notpad link : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()
print("\033[1;33;40m", end = "")
print("\033[1;34;40m", end = "")
sp('\33[1m'"\nEnter your name :►\n")
yyy= str(input())
print("\033[1;34;40m", end = "")

msg6= int(input("➣Enter TIME : "))

os.system('clear')

sys.stdout.flush()

print(' F9IISU  v1.0')

count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(yyy+ ' ' +line)

            print(' Chala Gaya Comment :) - ', yyy+ ' ' +line, "\n")

            count += 1

            if count % 10 == 0:

                sleep(1)
