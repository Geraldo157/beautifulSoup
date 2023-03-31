from bs4 import BeautifulSoup
import requests

url = "https://www.zoom.com.br/celular/smartphone-apple-iphone-11-128gb-ios?_lc=213"

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

strong = doc.find('strong', attrs={'class': 'Text_Text__h_AF6 Text_DesktopHeadingM__C_e4f'})
print(strong.string)
