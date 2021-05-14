import re
import requests
import bs4
import urllib.parse as urlparse
# XKCD Karikatürlerini indirme uygulaması


def download_XKCD_comic(imageurl, id):
    "Karikatürü indir ve idsi ile isimlendir"

    res = requests.get(imageurl)
    res.raise_for_status()
    with open('downloaded_comics/comic_'+id+'.png', 'wb') as comic:
        comic.write(res.content)

    print('İndirilen Karikatür: ' + id)


def get_XKCD_comic(url='https://xkcd.com/'):
    "Karikatür sayfasını gezin, bir önceki karikatürün sayfasını döndür"
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Karikatürün ID'sini bul
    middle_container = soup.select_one('#middleContainer')
    id = re.findall(
        r'Permanent link to this comic: https://xkcd.com/(\d+)/', middle_container.text)[0]

    imageurl = 'https:' + soup.select('#comic > img')[0].get('src')

    download_XKCD_comic(imageurl, id)

    # Prev butonuna basınca gelen karikatürün linkini ver. (Bir önceki karikatür.)
    return urlparse.urljoin('https://xkcd.com/', soup.find('a', text='< Prev').get('href'))


iteration = int(input('Kaç karikatür indirmek istiyorsunuz:'))
url = get_XKCD_comic()
for i in range(iteration-1):
    url = get_XKCD_comic(url)
