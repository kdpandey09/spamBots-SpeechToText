import pyautogui as pg
import webbrowser as wb
import time
while True:
    message = str(input("Enter The Message You Want To Send \n"))
    spam_number= int(input("how many times you want the message to be sent \n"))
    sleep_time = int(input("enter the time in seconds after which spam starts \n"))
    b = len(message)

    if b > 0 :
        url= "https://www.instagram.com/direct/inbox/"
        chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        wb.register("chrome",None,wb.BackgroundBrowser(chrome_path))
        wb.get("chrome").open(url)
        time.sleep(sleep_time)
        spam = []
        spam = message.split()
        for p in range(spam_number):
             for i in spam:
                pg.typewrite(i)
                pg.press("enter")
        break
    else:
        print("Don't Enter a Null Messages")
        continue