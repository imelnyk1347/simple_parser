import requests
from bs4 import BeautifulSoup
import os


def get_html():
    # import pdb;pdb.set_trace()
    url = 'https://bank.gov.ua/ua/markets/exchangerates?date=20.11.2020&period=daily'
    r = requests.get(url)
    return r.text


def get_value_args(html):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find('td', text='USD').find_parent('tr').find_all('td')[-1].text
    return result


def send_message(message):
    title = 'Dollar USA'
    os.system(f'notify-send "{title}" "{message}"')


def main():
    rate = get_value_args(get_html())
    send_message(rate)


if __name__ == '__main__':
    main()
