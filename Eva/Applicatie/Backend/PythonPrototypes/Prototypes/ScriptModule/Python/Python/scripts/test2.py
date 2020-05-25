import requests
from bs4 import BeautifulSoup

decoratedFunction="test"

def test():
    # Collect and parse first page
    page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    soup = BeautifulSoup(page)

    # Pull all text from the BodyText div
    artist_name_list = soup.find('body')

    # Pull text from all instances of <a> tag within BodyText div
    artist_name_list_items = artist_name_list.find_all('a')
    for artist_name in artist_name_list_items:
        print(artist_name.prettify())
