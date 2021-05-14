import bs4
import requests
import re


def getAmazonPrice(amazon_url):
    'Request a response, then check for errors'
    res = requests.get(amazon_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    # CSS Selector kullanarak bir elemente ulaş.
    #
    # NOT: CSS Selector'u site güncellendikçe veya ürüne göre değişebilir.
    # Bu yüzden ürün fiyatlarına ulaşmak için bir api kullanılması daha doğru olur
    price = soup.select_one('#price')

    return price.text.strip()


url_regex = re.compile(r'(.*)\??')
url = url_regex.search(input('Input the url: ')).group(1)
print('the url is ', url)
print('The price is', getAmazonPrice(url))
