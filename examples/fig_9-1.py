from time import sleep
from collections import Counter
from bs4 import BeautifulSoup
import re
import requests

base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
    "data.do?sortby=publicationDate&page="

books = []

NUM_PAGES = 31

def is_video(td):
    """it's a video if it has exactly one pricelabel, and if
    the stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and
        pricelabels[0].text.strip().startswith("Video"))

def book_info(td):
    title = td.find('div', 'thumbheader').a.text
    by_author = td.find('div', 'AuthorName').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(',')]
    isbn_link = td.find('div', 'thumbheader').a.get('href')
    isbn = re.match('/product/(.*)\.do', isbn_link).groups()[0]
    date = td.find('span', 'directorydate').text.strip()

    return {
        'title': title,
        'authors': authors,
        'isbn': isbn,
        'date': date
    }

def get_year(book):
    return int(book['date'].split()[1])

for page_num in range(1, NUM_PAGES + 1):
    print "souping page", page_num, ",", len(books), " found so far"
    url = base_url + str(page_num)
    soup = BeautifulSoup(requests.get(url).text, 'html5lib')

    for td in soup('td', 'thumbtext'):
        if not is_video(td):
            books.append(book_info(td))

    sleep(30)

year_counts = Counter(get_year(book) for book in books
    if get_year(book) <= 2014)

import matplotlib.pyplot as plt
years = sorted(year_counts)
book_counts = [year_counts[year] for year in years]
plt.plot(years, book_counts)
plt.ylabel('# of data books')
plt.title('Data is Big!')
plt.show()
