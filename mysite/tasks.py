from mysite.mysite.bolignyt.models import PythonBolig
from bs4 import BeautifulSoup
import requests
from django.utils import timezone


def build_bolig_search_url():
    urlformat = "http://www.dba.dk/boliger/ejerbolig/side={side}/"
    url = []
    for num in range(11):
        next_page = str(num)
        url.append(urlformat.format(side=next_page))
    return url


def get_bolig_details():
    time = timezone.now()
    bolig_details = []
    for url in build_bolig_search_url():
        b = requests.get(url)
        soup = BeautifulSoup(b.content, "html.parser")
        get_date = soup.find_all("td", {"title": "Dato"})
        get_price = soup.find_all("td", {"title": "Pris"})
        get_url = soup.find_all('a', 'listingLink')['href']
        get_description = soup.find_all('div', 'expandable-box expandable-box-collapsed')
        for date, price, url, description in map(None,
                                                 get_date,
                                                 get_price,
                                                 get_url,
                                                 get_description):
            bolig_url = date.contents[3].attrs['content']
            bolig_description = description.contents[1].attrs['content']
            date_posted = date.attrs['content']
            price = price.text.encode("utf-8")
            date_found = time
            bolig_records = {'Url': bolig_url, 'date_found': date_found, 'Price': price,
                             'Description': bolig_description}
            bolig_details.append(bolig_records)
    return bolig_details


def save_bolig():
    for boliger in get_bolig_details():
        if not PythonBolig.objects.filter(date_found=boliger['date_found'], Price=boliger['Price'], Url=boliger['Url'],
                                          Description=boliger['Description']).exists():
            bolig = PythonBolig(
                date_found=boliger['date_found'],
                Price=boliger['Price'],
                Url=boliger['Url'],
                Description=boliger['Description']
            )
            bolig.save()
    return
