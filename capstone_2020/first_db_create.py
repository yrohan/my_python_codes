from bs4 import BeautifulSoup
import requests
import time
import os.path
import re
import pandas as pd


def check_subtag(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tag = soup.find("div", class_="summary_text").find("a")
    if tag:
        return True
    else:
        return False


def aka(url):
    try:
        mov_page = requests.get(url)
    except:
        return "not able to get"
    soup = BeautifulSoup(mov_page.text, 'html.parser')
    mov_en_title = soup
    mov_en_titles = soup.find_all("div", class_="txt-block")
    for i in range(0, len(mov_en_titles)):
        tmp = mov_en_titles[i].h4
        exp = str(tmp)
        # print(exp.h4)
        # print("\n")
        # print("exp is <h4 class=\"inline\">Also Known As:</h4>")
        if exp == "<h4 class=\"inline\">Also Known As:</h4>":
            mov_en_title = mov_en_titles[i]

    tmp_aka = mov_en_title.contents[2]
    clean_aka = tmp_aka
    clean_aka = re.sub(r"\n", "", clean_aka)
    movie_aka = clean_aka
    return movie_aka


def get_imd_summary_subtag(url):
    try:
        movie_page = requests.get(url)
    except:
        return "not able to get"
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    summary1 = soup.find("div", class_="summary_text").contents[0].strip()
    summary2 = soup.find("div", class_="summary_text").find("a").contents
    summary3 = soup.find("div", class_="summary_text").contents[2].strip()
    temp_summary = summary1 + ' ' + summary2[0] + summary3
    clear_summary = str(temp_summary)
    movie_summary = clear_summary.replace(r",", "")
    return movie_summary


def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("h3", class_="lister-item-header")
    return movies


def get_imd_summary(url):
    try:
        movie_page = requests.get(url)
    except:
        return "not able to get"
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tmp_summary = soup.find("div", class_="summary_text").contents[0].strip()
    clean_summary = str(tmp_summary)
    mov_summary = clean_summary.replace(r",", "")
    return mov_summary


def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.find("span", class_="lister-item-year text-muted unbold").text
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url


def imd_movie_picker():
    ctr = 0
    print("--------------------------------------------")
    for movie in get_imd_movies('https://www.imdb.com/search/title/?title_type=feature&languages=en&adult=include'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        if check_subtag(movie_url):
            movie_summary = get_imd_summary_subtag(movie_url)
        else:
            movie_summary = get_imd_summary(movie_url)
        tmp_aka = aka(movie_url)
        clean_aka = tmp_aka
        clean_aka = re.sub(r"\n", "", clean_aka)
        clean_aka = re.sub(r"\t", "", clean_aka)
        movie_aka = clean_aka.encode('utf-8')
        movie_title = movie_title.encode('utf-8')
        movie_aka = movie_aka.decode('utf-8')
        movie_title = movie_title.decode('utf-8')
        movie_year = movie_year[1:-1]
        print(movie_title, "(", movie_aka, ")", movie_year)
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
        db_file1 = open("imdb_movies.csv", "w", encoding='utf-8')
        db_file1.write("Title,AKA,Year,Link,Summary\n")
    url_file = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/datasets/url.csv")
    for i in range(0, 2):
        url = url_file["url"][i]
        for movie in get_imd_movies(url):
            movie_title, movie_year, movie_url = get_imd_movie_info(movie)
            if check_subtag(movie_url):
                movie_summary = get_imd_summary_subtag(movie_url)
            else:
                movie_summary = get_imd_summary(movie_url)
            movie_title = re.sub(r",", "", movie_title)
            tmp_aka = aka(movie_url)
            clean_aka = tmp_aka
            clean_aka = re.sub(r",", "", clean_aka)
            clean_aka = re.sub(r"\n", "", clean_aka)
            clean_aka = clean_aka[1:-6]
            movie_aka = str(clean_aka.encode('utf-8'))
            movie_title = str(movie_title.encode('utf-8'))
            if len(movie_year) > 6 and movie_year[5] == "(":
                print(" 7 ", movie_year[6:-1])
                movie_year = str(movie_year[6:-1])
            elif len(movie_year) > 6 and movie_year[5] != "(" :
                print(" 6 ",movie_year[5:-1])
                movie_year = str(movie_year[5:-1])
            else:
                movie_year = str(movie_year[1:-1])
            db_file1.write(movie_title)
            db_file1.write(",")
            db_file1.write(movie_aka)
            db_file1.write(",")
            db_file1.write(movie_year)
            db_file1.write(",")
            db_file1.write(movie_url)
            db_file1.write(",")
            db_file1.write(movie_summary)
            db_file1.write("\n")
            ctr = ctr + 1
            if ctr == 50:
                break;
        time.sleep(2)

    db_file1.close()


if __name__ == '__main__':
    # imd_movie_picker()
    imd_movie_db_create()
    print("\nExecution was successfull")
