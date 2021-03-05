import requests
import urllib.request
from bs4 import BeautifulSoup


def download(url, path, name):
    # print('url =', url)
    # print('path =', path)
    # print('name =', name)
    urllib.request.urlretrieve(url, path + name)
    print('Downloaded file:', name)


def get_operators(table):
    td = table.find_all('td', rowspan='2')


def get_images(url, type):
    print('Downloading', type, 'images ...')

    # get html
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', class_='article-table')

    imgs = table.find_all('img')
    for img in imgs:
        # print(img)
        if 'data-src' in img:
            print(img)
        filename = img.get('data-image-key')
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

        print()

    # end download
    print('====== IMAGE DOWNLOAD SUCCESSFULLY ======')


def main():
    url = 'https://babaiswiki.fandom.com/wiki/Category:Properties'
    # test(url)
    get_images(url, 'operators')


if __name__ == '__main__':
    main()
