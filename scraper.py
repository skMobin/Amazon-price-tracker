import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL ="https://www.amazon.in/Apple-MR972HN-15-4-inch-i7-8850H-Integrated/dp/B07G49GQ56/ref=sr_1_1?crid=R6QFV5T6ANWN&keywords=macbook+pro+15+inch&qid=1578064736&sprefix=mac%2Caps%2C279&sr=8-1"


headers = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
def checkPrice():
    page = requests.get(URL,headers =headers)

    soup = BeautifulSoup(page.content,"html.parser")
    price = soup.find(id="priceblock_ourprice").get_text()

    price = float(price[1:13].replace(',',''))
    print(price)
    if( price > 200000.00):
        sendEmail()
    else:
        print("There's no down in price")
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("email","password")

    subject = 'HEY check the Price!!!'
    body = "check the link \n"+ URL
    print(body)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('sender email','reciever email',msg)
    print("Check Your E-mail")
    server.quit()

while True:
    checkPrice()
    time.sleep("mention any intervalhere at you want to check the price eg: 60*60 would one hour ")
    #kill the program later whenever you want to stop ;)