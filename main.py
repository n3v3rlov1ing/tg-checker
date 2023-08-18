import requests
from bs4 import BeautifulSoup

with open('usernames.txt', 'r') as f:
    usernames = f.read().split('\n')
    for i in usernames: 
        url = f'https://t.me/{i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        get_username = soup.find_all('div', class_ = "tgme_page_extra")
        for n in get_username:
            clear_username = n.text.split('@')
            clear_username = clear_username[1].replace('\n','')
            if clear_username:
                with open('good.txt', 'a') as f:
                    f.write(f'{clear_username}\n')