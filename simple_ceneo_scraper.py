from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, select, update

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/myapp')

produkty = Table(
    'produkty', MetaData(),
    Column('SKU', String(255)),
    Column('Ceneo_ID', Integer),
    Column('Ceneo_Cena', Float)
)


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        price = soup.find('p', class_='my-0')
        if price:
            price_text = price.find(class_="price-format nowrap")
            if price_text:
                try:
                    return float(price_text.text.strip().replace('zł', '').replace(',', '.').replace(' ', ''))
                except ValueError:
                    pass
    return None


def update_price_in_db(ceneo_id, price):
    if price is not None:
        sql_stmt = update(produkty).where(produkty.columns.Ceneo_ID == ceneo_id).values(Ceneo_Cena=price)
        with engine.begin() as conn:
            conn.execute(sql_stmt)


def main():
    lista_SKU = []

    with engine.connect() as connection:
        query = select(produkty.columns.SKU, produkty.columns.Ceneo_ID).where(
            produkty.columns.Ceneo_ID != None)
        result = connection.execute(query)
        for row in result:
            lista_SKU.append(row[1])

    base_url = 'https://www.ceneo.pl/'

    for ceneo_id in lista_SKU:
        current_url = base_url + str(ceneo_id)
        price = get_html(current_url)
        update_price_in_db(ceneo_id, price)


if __name__ == "__main__":
    main()