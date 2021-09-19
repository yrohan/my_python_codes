from bs4 import BeautifulSoup
import requests
import random
import os.path
import re
import pickle


def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies


def subtitle_dict():
    dbfile = open('C:/Users/Linux/PycharmProjects/capstone_2020/datasets/subdict.pkl', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys,'=>',db[keys])

    '''ctr = 0
    print("--------------------------------------------")
    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        tmp_aka = aka(movie_url)

        movie_title = movie_title.encode("utf-8")
        movie_year = movie_year.encode("utf-8")
        movie_year = movie_year[1:-1]
        print(movie_title + "(" + movie_aka + ")" + movie_year)
        print(movie_summary)
        print("--------------------------------------------")
        ctr = ctr + 1
        if ctr == 10:
            break;'''


def check_subtag(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tag = soup.find("div", class_="summary_text").find("a")
    if tag:
        return True
    else:
        return False


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
    print(mov_en_title.contents)
    print("{" + mov_en_title.contents[2] + "}")
    print("\n")
    return mov_en_title.contents[2]
    '''clean_aka = tmp_aka.encode("utf-8")
    clean_aka = re.sub(r"\n", "", clean_aka)
    print("\n After Encode :")  printing output to check for improvements
    print("{"+clean_aka+"}")
    movie_aka = clean_aka.decode("utf-8")
    movie_aka = re.sub(r"\n", "", movie_aka)
    movie_aka = movie_aka.strip(u' ')
    print("\n After Decode :")
    print("["+movie_aka+"]")
    return movie_aka'''


def get_imd_summary_subtag(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    summary1 = soup.find("div", class_="summary_text").contents[0].strip()
    summary2 = soup.find("div", class_="summary_text").find("a").contents
    summary3 = soup.find("div", class_="summary_text").contents[2].strip()
    temp_summary = summary1 + ' ' + summary2[0] + summary3
    clear_summary = str(temp_summary)
    movie_summary = clear_summary.replace(r",", "")
    return movie_summary


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tmp_summary = soup.find("div", class_="summary_text").contents[0].strip()
    clean_summary = tmp_summary.encode('utf-8')
    mov_summary = clean_summary.replace(r",", "")
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
        tmp_aka = aka(movie_url)
        clean_aka = tmp_aka.encode("utf-8")
        clean_aka = re.sub(r"\n", "", clean_aka)
        print("\n After Encode :")  # printing output to check for improvements
        print("{" + clean_aka + "}")
        movie_aka = clean_aka.decode("utf-8")
        movie_aka = re.sub(r"\n", "", movie_aka)
        print("\n After Decode :")
        print("[" + movie_aka + "]")
        movie_title = movie_title.encode("utf-8")
        movie_year = movie_year.encode("utf-8")
        movie_year = movie_year[1:-1]
        print(movie_title + "(" + movie_aka + ")" + movie_year)
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
        movie_aka = aka(movie_url)
        movie_title = movie_title.encode("utf-8")
        movie_year = movie_year.encode("utf-8")
        movie_year = movie_year[1:-1]
        db_file1.write(movie_title + "," + movie_aka + "," + movie_year + "," + movie_url + "," + movie_summary)
        db_file1.write("\n")
        ctr = ctr + 1
        if ctr == 7:
            break;

    db_file1.close()


if __name__ == '__main__':
    imd_movie_picker()
    subtitle_dict()
    # imd_movie_db_create()
    print("\nExecution was successfull")
