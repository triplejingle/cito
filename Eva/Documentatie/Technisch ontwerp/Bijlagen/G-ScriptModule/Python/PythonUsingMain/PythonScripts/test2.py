import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # Collect and parse first page
    page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pull all text from the BodyText div
    artist_name_list = soup.find(class_='BodyText')

    # Pull text from all instances of <a> tag within BodyText div
    artist_name_list_items = artist_name_list.find_all('a')
    for artist_name in artist_name_list_items:
        print(artist_name.prettify())
