from bs4 import BeautifulSoup
import requests
import random


def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()


def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url


def aka(url):
    mov_page = requests.get(url)
    soup = BeautifulSoup(mov_page.text, 'html.parser')
    mov_en_title = soup
    mov_en_titles = soup.find_all("div", class_="txt-block")
    i = 0
    # k = 0
    for i in range(0, len(mov_en_titles)):
        tmp = mov_en_titles[i].h4
        exp = str(tmp)
        # print(exp.h4)
        # print("\n")
        # print("exp is <h4 class=\"inline\">Also Known As:</h4>")
        if exp == "<h4 class=\"inline\">Also Known As:</h4>":
            mov_en_title = mov_en_titles[i]
            # k = i
            # print(mov_en_titles[i])
            # print(exp)

    print("\n Translation")
    print(mov_en_title.contents[2])
    print("\n")


def imd_movie_picker():
    ctr = 0
    print("--------------------------------------------")
    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        # print("\n Movie is ")
        # print(movie.a.text)
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        aka(movie_url)
        # en_text=
        # print("\n English Translation : ")
        # print(en_text)
        # print("\n")
        print(movie_title, movie_year)
        print(movie_summary)
        print("--------------------------------------------")
        ctr = ctr + 1
        if (ctr == 10):
            break;


if __name__ == '__main__':
    imd_movie_picker()
