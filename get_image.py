import requests
import urllib.request
import os
from bs4 import BeautifulSoup

types = ['nouns', 'operators', 'properties']
base_url = 'https://babaiswiki.fandom.com/wiki/'


def download(url, path, name):
    urllib.request.urlretrieve(url, path + name)
    print('Downloaded file:', name)


def get_nouns(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    imgs = table.find_all('kimg')

    try:
        os.mkdir('./gif/characters')
        os.mkdir('./gif/nouns')
    except:
        pass

    for img in imgs:
        filename = img.get('data-image-key')
        fileSrc = img.get('data-src')
        if 'Text' in filename:
            download(fileSrc, './nouns/', filename)
        else:
            download(fileSrc, './characters/', filename)


def get_operators(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    tds = table.find_all('td')

    try:
        os.mkdir('./gif/operators')
    except:
        pass

    for td in tds:
        if 'rowspan' in td.attrs:
            img = td.find('img')
            filename = img.get('data-image-key')
            filesrc = ''
            if 'data-src' in img.attrs:
                filesrc = img.get('data-src')
            else:
                filesrc = img.get('src')

            print(filename)
            print(filesrc)
            download(filesrc, './operators/', filename)


def get_properties(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    tds = table.find_all('td')

    try:
        os.mkdir('./gif/operators')
    except:
        pass

    for td in tds:
        if 'style' in td.attrs:
            img = td.find('img')
            filename = img.get('data-image-key')
            if 'data-src' in img.attrs:
                fileSrc = img.get('data-src')
            else:
                fileSrc = img.get('src')
            download(fileSrc, './properties/', filename)


def main():
    for type in types:
        select = input(
            'Do you want to download gifs for ' + type + '? (Y/n) ')
        if select == 'N' or select == 'n':
            continue

        try:
            os.mkdir('./gif')
        except:
            pass

        print('Downloading ' + type + '...')
        if type == types[0]:
            get_nouns(base_url + 'Category:Nouns')
        elif type == types[1]:
            get_operators(base_url + 'Category:Operators')
        elif type == types[2]:
            get_properties(base_url + 'Category:Properties')
        print('Download successful for ' + type +
              ', files are located in ./gif/' + type)


if __name__ == '__main__':
    main()
