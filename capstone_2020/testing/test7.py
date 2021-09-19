from bs4 import BeautifulSoup
import requests


def check_subtag(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tag = soup.find("div", class_="summary_text").find("a")
    if tag:
        return True
    else:
        return False


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    summary1 = soup.find("div", class_="summary_text").contents[0].strip()
    summary2 = soup.find("div", class_="summary_text").find("a").contents
    summary3 = soup.find("div", class_="summary_text").contents[2].strip()
    movie_summary = summary1 + ' ' + summary2[0] + summary3

    return movie_summary


def get_imd_movie_info(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    raw_movie_title = soup.title.string
    movie_year = "2019"
    return raw_movie_title, movie_year


if __name__ == '__main__':
    test_url = 'https://www.imdb.com/title/tt4154796/'
    mov_title, mov_year = get_imd_movie_info(test_url)
    val=check_subtag(test_url)
    print("\n")
    print(val)
    mov_summary = get_imd_summary(test_url)
    mov_title = mov_title.encode("utf-8")
    print("\n")
    print(mov_title, mov_year)
    print("\n")
    print(mov_summary)
    print("Done")
