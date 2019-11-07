import requests
from bs4 import BeautifulSoup as bs

headers = 'http://www.ip-adress.com/proxy_list/'
z_url = 'https://www.zakon.kz/news'

def news_pars():
    session = requests.Session()
    request = session.get(z_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, "lxml")
        hours_table = soup.find('div', attrs={'id': 'dle-content'})
        print(hours_table)

        #news_info = 

news_pars()