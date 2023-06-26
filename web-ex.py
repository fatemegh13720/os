import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

start = time.time()


def finder1():
    url = "https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE~Category~40"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('.maintitle')
    price = soup.select('.prd-price span')

    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['قیمت', 'نام'])
    df = df.dropna()
    print(df)

    high_price_phone = df.loc[df['نام'].idxmax()]
    low_price_phone = df.loc[df['نام'].idxmin()]

    print("\nگران‌ترین لپتاپ: ", high_price_phone['نام'])
    print("ارزان‌ترین لپتاپ: ", low_price_phone['نام'])


def finder2():
    url = "https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA_%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE~Category~40~page~3"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.select('.maintitle')
    price = soup.select('.prd-price span')


    list_title = [t.text for t in title]
    list_price = [int(p.text.replace(',', '')) for p in price]

    database = dict(list(zip(list_title, list_price)))

    df = pd.DataFrame(list(database.items()), columns=['قیمت', 'نام'])
    df = df.dropna()
    print(df)

    high_price_phone = df.loc[df['نام'].idxmax()]
    low_price_phone = df.loc[df['نام'].idxmin()]

    print("\nگران‌ترین لپتاپ: ", high_price_phone['نام'])
    print("ارزان‌ترین لپتاپ: ", low_price_phone['نام'])


finder1()
finder2()
end = time.time()
print(end - start)
