import requests
import urllib.request
from bs4 import BeautifulSoup


def download(url, path, name):
    urllib.request.urlretrieve(url, path + name)
    print('Downloaded file:', name)


def get_operators(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    tds = table.find_all('td')

    for td in tds:
        if 'rowspan' in td.attrs:
            img = td.find('img')
            filename = img.get('data-image-key')
            fileSrc = ''
            if 'data-src' in img.attrs:
                fileSrc = img.get('data-src')
            else:
                fileSrc = img.get('src')

            print(filename)
            print(fileSrc)
            download(fileSrc, './operators/', filename)
    print('====== DOWNLOAD SUCCESSFULLY ======')


def get_nouns(url):
    print('Getting nouns ...')
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    imgs = table.find_all('img')

    for img in imgs:
        filename = img.get('data-image-key')
        fileSrc = img.get('data-src')
        if 'Text' in filename:
            download(fileSrc, './nouns/', filename)
        else:
            download(fileSrc, './characters/', filename)

    print('====== DOWNLOAD SUCCESSFULLY ======')


def get_properties(url):
    print('Getting properties ...')
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    tds = table.find_all('td')

    for td in tds:
        if 'style' in td.attrs:
            img = td.find('img')
            filename = img.get('data-image-key')
            if 'data-src' in img.attrs:
                fileSrc = img.get('data-src')
            else:
                fileSrc = img.get('src')
            download(fileSrc, './properties/', filename)
    print('====== DOWNLOAD SUCCESSFULLY ======')


def main():
    url_nouns = 'https://babaiswiki.fandom.com/wiki/Category:Nouns'
    url_op = 'https://babaiswiki.fandom.com/wiki/Category:Operators'
    url_props = 'https://babaiswiki.fandom.com/wiki/Category:Properties'
    # get_operators(url_op)
    # get_nouns(url_nouns)
    # get_properties(url_props)


if __name__ == '__main__':
    main()
