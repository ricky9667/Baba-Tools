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


def get_nouns(url):
    print('Getting nouns ...')
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')
    imgs = table.find_all('img')

    for img in imgs:
        filename = img.get('data-image-key')
        if 'Text' in filename:
            download(img.get('data-src'), './nouns/', filename)
        else:
            download(img.get('data-src'), './characters/', filename)

    print('====== DOWNLOAD SUCCESSFULLY ======')


def get_images(url, type):
    print('Downloading', type, 'images ...')

    # get html
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')

    # get operator images
    get_operators(table)

    # imgs = table.find_all('img')
    # for img in imgs:
    # print(img)
    # if 'data-src' in img:
    # print(img)
    # filename = img.get('data-image-key')
    # print(img.attrs)

    # download nouns
    # if 'Text' in filename:
    #     download(img.get('data-src'), './nouns/', filename)
    # else:
    #     download(img.get('data-src'), './characters/', filename)

    # download properties
    # if 'data-src' in img.attrs:
    # download(img.get('src'), './properties/', filename)
    # print(img)

    # download operators

    # print()

    # end download
    print('====== IMAGE DOWNLOAD SUCCESSFULLY ======')


def main():
    url_nouns = 'https://babaiswiki.fandom.com/wiki/Category:Nouns'
    url_op = 'https://babaiswiki.fandom.com/wiki/Category:Operators'
    url_props = 'https://babaiswiki.fandom.com/wiki/Category:Properties'
    # get_operators(url_op)
    get_nouns(url_nouns)


if __name__ == '__main__':
    main()
