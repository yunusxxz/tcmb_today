import requests as req
import lxml
from bs4 import BeautifulSoup as bs

url = 'https://www.tcmb.gov.tr/kurlar/today.xml'

response = req.get(url)

if response.status_code == 200:
    content = response.content
    soup = bs(content, 'xml')
    currencies = soup.find_all('Currency')
    # print(currencies)
    codes = [c['CurrencyCode'] for c in currencies]
    #print(codes)
    currency_dict = []
    for c in currencies:
        item = {
            "code": c['CurrencyCode'],
            "name": c.find('CurrencyName').text.strip(),
            "ForexBuying": float(c.find('ForexBuying').text if c.find("ForexBuying").text else 0),
            "ForexSelling": float(c.find('ForexSelling').text if c.find("ForexSelling").text else 0),
            "BanknoteBuying": float(c.find('BanknoteBuying').text if c.find("BanknoteBuying").text else 0),
            "BanknoteSelling": float(c.find("BanknoteSelling").text if c.find("BanknoteSelling").text else 0)

        }

        currency_dict.append(item)
        print(currency_dict)
