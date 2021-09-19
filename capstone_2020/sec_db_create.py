from bs4 import BeautifulSoup
import requests
import os.path
import re


def check_subtag(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tag = soup.find("div", class_="summary_text").find("a")
    if tag:
        return True
    else:
        return False


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


def get_all_reviews(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tag1 = soup.find_all("a", class_="title")
    tag2 = soup.find_all("div", class_="text show-more__control")
    tag3 = soup.find_all("div", class_="lister-item-content")
    for i in range(0, 5):
        small_comment = tag1[i].text
        full_review = tag2[i].text
        subtag1 = tag3[i].find_all("span")
        print("\nSmall Comment ", small_comment)
        print("\nFull Review ", full_review)
        if len(subtag1) > 5:
            imdb_user_rating = subtag1[len(subtag1) - 5].text
            total_rating = subtag1[len(subtag1) - 4].text
            print("\nIMDB User Rating ", imdb_user_rating, total_rating)
        else:
            print("No User Ratings")


def get_mov_reviews(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tag1 = soup.find("div", class_="user-comments")
    all_rev_url = url
    if tag1:
        tag2 = tag1.find_all("a")
        if tag2:
            all_rev_url = "http://www.imdb.com" + tag2[len(tag2) - 1]['href']
            # print("\n All reviews Url ", tag2[len(tag2)-1].text ," ", all_rev_url)
        '''else:
            small_comment = tag1.span.strong.text
            full_review = tag1.p.text
            print("\nSmall Comment ", small_comment)
            print("\nFull Review ", full_review)'''
    else:
        all_rev_url = "No Reviews found for this Movie"
    return all_rev_url


def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find("h3", class_="lister-item-header")
    return movies


def get_imd_summary(url):
    movie_page = requests.get(url)
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
        movie_summary = get_imd_summary(movie_url)
        movie_title = movie_title.encode('utf-8')
        movie_title = movie_title.decode('utf-8')
        movie_year = movie_year
        print(movie_title, movie_year)
        print(movie_summary)
        get_mov_reviews(movie_url)
        print("--------------------------------------------")
        ctr = ctr + 1
        if ctr == 1:
            break;


def file_check():
    fcheck = os.path.isfile("C:/Users/Linux/PycharmProjects/capstone_2020/movie_reviews.csv")
    return fcheck


def imd_movie_db_create():
    ctr = 0
    val = file_check()
    if val:
        db_file1 = open("movie_reviews.csv", "a")
    else:
        db_file1 = open("movie_reviews.csv", "w", encoding='utf-8')
        db_file1.write("Comment,Reviews,Summary,UsrRating,TotalRating,Name\n")

    movie = get_imd_movies('https://www.imdb.com/search/title/?title_type=feature&languages=en&adult=include')
    movie_title, movie_year, movie_url = get_imd_movie_info(movie)
    if check_subtag(movie_url):
        movie_summary = get_imd_summary_subtag(movie_url)
    else:
        movie_summary = get_imd_summary(movie_url)

    all_rev_url = get_mov_reviews(movie_url)
    if all_rev_url != "No Reviews found for this Movie":
        page = requests.get(all_rev_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        tag1 = soup.find_all("a", class_="title")
        tag2 = soup.find_all("div", class_="text show-more__control")
        tag3 = soup.find_all("div", class_="lister-item-content")
        movie_comment, movie_review, movie_user_rating, tot_rating = "No Comment", "No Review", "No Rating", "10"
        for i in range(0, len(tag1)):
            small_comment = tag1[i].text
            full_review = tag2[i].text
            subtag1 = tag3[i].find_all("span")
            print("\nSmall Comment ", small_comment)
            print("\nFull Review ", full_review)
            if len(subtag1) > 6:
                imdb_user_rating = subtag1[len(subtag1) - 6].text
                total_rating = subtag1[len(subtag1) - 5].text
                temp_rating = subtag1[len(subtag1)-4].text
                print("\nIMDB User Rating ", imdb_user_rating, total_rating,temp_rating)
            else:
                print("No User Ratings")
            movie_comment, movie_review, movie_user_rating, tot_rating = small_comment, full_review, imdb_user_rating, total_rating
            movie_comment = re.sub(r"\n","",movie_comment)
            movie_review = re.sub(r"\n", "",movie_review)
            movie_comment = re.sub(r",", "", movie_comment)
            movie_review = re.sub(r",", "", movie_review)
            movie_user_rating = re.sub(r"\n", "", movie_user_rating)
            db_file1.write(movie_comment)
            db_file1.write(",")
            db_file1.write(movie_review)
            db_file1.write(",")
            db_file1.write(movie_summary)
            db_file1.write(",")
            db_file1.write(movie_user_rating)
            db_file1.write(",")
            db_file1.write(tot_rating)
            db_file1.write(",")
            db_file1.write(temp_rating)
            db_file1.write("\n")
            ctr = ctr + 1
    else:
        db_file1.write(",")
        db_file1.write(all_rev_url)
        db_file1.write(movie_summary)
        db_file1.write(",,")
        db_file1.write("\n")

    db_file1.close()


if __name__ == '__main__':
    # imd_movie_picker()
    imd_movie_db_create()
    print("\nExecution was successfull")
