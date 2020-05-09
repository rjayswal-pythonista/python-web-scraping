import requests
from bs4 import BeautifulSoup


request = requests.get('https://www.flipkart.com/kellogg-s-corn-flakes-original/p/itmf7e2z7wun7zxe?'
                       'pid=CAFETEGHHY35F8YU&lid=LSTCAFETEGHHY35F8YUCIM32D&marketplace=FLIPKART&srno=b_'
                       '1_3&otracker=hp_creative_card_1_10.creativeCard.CREATIVE_CARD_I5ZQ2BR5C6FT&fm=neo%2'
                       'Fmerchandising&iid=2d0fadda-7195-498c-be8c-e549fed0e8a8.CAFETEGHHY35F8YU.' 
                       'SEARCH&ppt=browse&ppn=browse&ssid=szjbnd1h9s3ek1s01589001081867')
content = request.content
soup = BeautifulSoup(content, "html.parser")
element_name = soup.find("span", {"class": "_35KyD6"})#<span class="_35KyD6">Kellogg's Corn Flakes Original<!-- -->&nbsp;&nbsp;(475 g, Box)</span>
print(element_name.text.strip())
element_price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})    #<div class="_1vC4OE _3qQ9m1">₹175</div>
p = element_price.text.strip()
price = int(p[1:])

if price < 200:
    print(f'You should buy this item. Its price is {p}')
else:
    print(f'You should not buy this item. Its price is {p}, which is more than 200')
