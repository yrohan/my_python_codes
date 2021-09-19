from bs4 import BeautifulSoup
import requests
import random
import os.path
import re


def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tmp_summary = soup.find("div", class_="summary_text").contents[0].strip()
    clean_summary = str(tmp_summary)
    #print("\n After cleaning : ")
    mov_summary = clean_summary.replace(r",","")
    #print("\n")
    return mov_summary



def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url


def imd_movie_picker():
    ctr = 0
    print("--------------------------------------------")
    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        movie_title = movie_title.encode("utf-8")
        movie_year = movie_year.encode("utf-8")
        movie_year = movie_year[1:-1]
        print(movie_title, movie_year)
        print(movie_summary)
        print("--------------------------------------------")
        ctr = ctr + 1
        if ctr == 10:
            break;


def file_check():
    fcheck = os.path.isfile("C:/Users/Linux/PycharmProjects/capstone_2020/imdb_movies.csv")
    return fcheck


def imd_movie_db_create():
    ctr = 0
    val = file_check()
    if val:
        db_file1 = open("imdb_movies.csv", "a")
    else:
        db_file1 = open("imdb_movies.csv", "w")
        db_file1.write("Title,AKA,Year,Link,Summary\n")

    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        movie_title = movie_title.encode("utf-8")
        movie_year = movie_year.encode("utf-8")
        movie_year = movie_year[1:-1]
        db_file1.write(movie_title + "," + movie_year + "," + movie_url + "," + movie_summary)
        db_file1.write("\n")
        ctr = ctr + 1
        if ctr == 7:
            break;

    db_file1.close()


if __name__ == '__main__':
    imd_movie_picker()
    #imd_movie_db_create()
    print("\nExecution was successfull")
