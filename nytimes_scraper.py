import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime


def ny_times_lists():
    """
    This function uses BeautifulSoup to scrape nytimes best business books from
    2014 to 2019
    """

    nylist_2014to2019 = pd.DataFrame(columns=['Date', 'Title', 'Author', 'Ranking', 'Year', 'Month'])

    for year in range(2014, 2020):
        for month in range(1, 13):
            nytimes_link = f'https://www.nytimes.com/books/best-sellers/{year}/{month:02}/01/business-books/'
            nytimes_biz_book = requests.get(nytimes_link)
            soup = BeautifulSoup(nytimes_biz_book.text, "html.parser")
            book_list = soup.findAll('div', {'class': 'css-xe4cfy'})

            for rank, book in enumerate(book_list):
                ranking: int = rank + 1
                book_title = book.find('h3').text.title()
                if len(book_title) >= 30:
                    space: int = book_title[:15].rfind(' ')
                    book_title = book_title[:space] + '\n' + book_title[space + 1:]
                    space = book_title[:30].rfind(' ')
                    book_title = book_title[:space] + '\n' + book_title[space + 1:]
                elif 30 > len(book_title) > 15:
                    space = book_title[:15].rfind(' ')
                    book_title = book_title[:space] + '\n' + book_title[space + 1:]
                book_author = book.find('p', {'class': 'css-hjukut'}).text[3:]
                date = datetime.date(year=year, month=month, day=1)
                book_data = pd.Series([date, book_title, book_author, ranking, year, month],
                                      index=['Date', 'Title', 'Author', 'Ranking', 'Year', 'Month'])
                nylist_2014to2019 = nylist_2014to2019.append(book_data, ignore_index=True, sort=False)

    nylist_2014to2019.to_json('nytimes_best_business_books_2014-2019.json')

    return nylist_2014to2019


if __name__ == "__main__":
    ny_times_lists()
