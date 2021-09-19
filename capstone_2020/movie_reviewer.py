from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys
import time
from bs4 import BeautifulSoup
import requests
import os.path
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords


all_stopwords = stopwords.words('english')


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


def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    tmp_summary = soup.find("div", class_="summary_text").contents[0].strip()
    clean_summary = str(tmp_summary)
    mov_summary = clean_summary.replace(r",", "")
    return mov_summary



def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("h3", class_="lister-item-header")
    return movies


def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.find("span", class_="lister-item-year text-muted unbold").text
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url


def file_check(file_name):
    fcheck = os.path.isfile("C:/Users/Linux/PycharmProjects/capstone_2020/" + file_name)
    return fcheck


def sentiment_analyzer_scores(text):
    good_word = ["phenomenal", "moved"]
    bad_word = ["garbage"]
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    compound_score = score['compound']
    all_word = word_tokenize(text)
    for i in range(0, len(all_word)):
        if all_word[i] in good_word:
            compound_score += 0.7
        if all_word[i] in bad_word:
            compound_score += -0.7

    return compound_score


def calc_score():
    plot_words = ["writing", "scene","cinematagraphy"]
    acting_words = ["acting", "performance","script",]
    sound_words = ["song","sound"]
    found_plot_words = []
    found_acting_words = []
    found_sound_words = []
    all_relevant_comm_words = []
    all_relevant_revw_words = []
    tot_acting_score = 0
    tot_plot_score = 0
    tot_sound_score = 0
    tot_comment_score = 0
    tot_review_score = 0
    review_data = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/movie_reviews.csv")
    row, column = review_data.shape
    if review_data["Reviews"][0] == "No Reviews found for this Movie":
        return 0,0,0,0
    else:
        for i in range(0, row):
            usr_comment = review_data["Comment"][i]
            usr_review = review_data["Reviews"][i]
            tot_comment_score = tot_comment_score + (sentiment_analyzer_scores(usr_comment) * int(review_data["UsrRating"][i]))
            tot_review_score = tot_review_score + (sentiment_analyzer_scores(usr_review) * int(review_data["UsrRating"][i]))
            comment_sent = sent_tokenize(usr_comment)
            rev_sent = sent_tokenize(usr_review)
            for sent in comment_sent:
                comment_words = word_tokenize(sent)
                for i in range(0, len(comment_words)):
                    comment_word = comment_words[i].lower()
                    if comment_word in acting_words:
                        found_acting_words.append(comment_word)
                        tot_acting_score += sentiment_analyzer_scores(sent)
                    if comment_word in plot_words:
                        found_plot_words.append(comment_word)
                        tot_plot_score += sentiment_analyzer_scores(sent)
                    if comment_word in sound_words:
                        found_sound_words.append(comment_word)
                        tot_sound_score += sentiment_analyzer_scores(sent)
            for sent in rev_sent:
                rev_words = word_tokenize(sent)
                for i in range(0, len(rev_words)):
                    rev_word = rev_words[i].lower()
                    if rev_word in acting_words:
                        found_acting_words.append(rev_word)
                        tot_acting_score += sentiment_analyzer_scores(sent)
                    if rev_word in plot_words:
                        found_plot_words.append(rev_word)
                        tot_plot_score += sentiment_analyzer_scores(sent)
                    if rev_word in sound_words:
                        found_sound_words.append(rev_word)
                        tot_sound_score += sentiment_analyzer_scores(sent)
            del comment_words
            del rev_words

        for i in range(0, row):
            usr_comment = review_data["Comment"][i]
            usr_review = review_data["Reviews"][i]
            comm_words = word_tokenize(usr_comment.lower())
            revw_words = word_tokenize(usr_review.lower())
            for i in range(0, len(comm_words)):
                if comm_words[i] not in all_stopwords:
                    all_relevant_comm_words.append(comm_words[i])
            for i in range(0, len(revw_words)):
                if revw_words[i] not in all_stopwords:
                    all_relevant_revw_words.append(revw_words[i])

        all_relevant_comm_words = list(set(all_relevant_comm_words))
        all_relevant_revw_words = list(set(all_relevant_revw_words))
        all_relevant_comm_words = [re.sub('\?|\'|!+|[0-9]+|#|>|=|\(|\)|\:', '', item) for item in all_relevant_comm_words]
        all_relevant_revw_words = [re.sub('\?|\'|!+|[0-9]+|#|>|=|\(|\)|\:', '', item) for item in all_relevant_revw_words]
        all_relevant_comm_words = [re.sub('[./-]', ' ', item) for item in all_relevant_comm_words]
        all_relevant_revw_words = [re.sub('[./-]', ' ', item) for item in all_relevant_revw_words]

        while ('' in all_relevant_comm_words):
            all_relevant_comm_words.remove('')
        while (' ' in all_relevant_comm_words):
            all_relevant_comm_words.remove(' ')
        while ('   ' in all_relevant_comm_words):
            all_relevant_comm_words.remove('   ')
        while ('' in all_relevant_revw_words):
            all_relevant_revw_words.remove('')
        while (' ' in all_relevant_revw_words):
            all_relevant_revw_words.remove(' ')

        tot_acting_score = round(((tot_acting_score / len(found_acting_words)) * 10), 1)
        tot_plot_score = round(((tot_plot_score / len(found_plot_words)) * 10), 1)
        tot_sound_score = round(((tot_sound_score / len(found_sound_words)) * 10), 1)
        tot_comment_score = round(((tot_comment_score / len(all_relevant_comm_words)) * 10), 1)
        tot_review_score = round(((tot_review_score / len(all_relevant_revw_words)) * 10), 1)
        if tot_acting_score > 10:
            tot_acting_score = 10
        if tot_plot_score > 10:
            tot_plot_score = 10
        if tot_sound_score > 10:
            tot_sound_score = 10
        if tot_review_score > 10:
            tot_review_score = 10
        else:
            tot_review_score += tot_comment_score
        if tot_comment_score+tot_review_score > 10:
            tot_review_score = 10

        return tot_acting_score, tot_plot_score, tot_sound_score, tot_review_score


def check_mov(name):
    found = False
    db_file1 = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/imdb_movies.csv")
    row, column = db_file1.shape
    print(row, column)
    print(name)
    name = re.sub(r"-"," ",name)
    mov_names = []
    for i in range(0, row):
        mov_name = db_file1["Title"][i]
        mov_name = re.sub(r"b", "", mov_name)
        mov_name = re.sub(r"'", "", mov_name)
        mov_name = re.sub(r'"', '', mov_name)
        mov_names.append(mov_name)
    for i in range(0, row):
        mov_name = db_file1["AKA"][i]
        mov_name = re.sub(r"b", "", mov_name)
        mov_name = re.sub(r"'", "", mov_name)
        mov_name = re.sub(r'"', '', mov_name)
        mov_names.append(mov_name)
    print(len(mov_names))
    print(mov_names)
    print(found)
    for i in range(0, len(mov_names)):
        mov_name = mov_names[i].lower()
        if name == mov_name or name == mov_names[i]:
            found = True
            break
    print(found)
    return found


def get_mov_url(name):
    url = "not found"
    name = re.sub(r"-", " ", name)
    print(name)
    db_file1 = pd.read_csv("C:/Users/Linux/PycharmProjects/capstone_2020/imdb_movies.csv")
    row, column = db_file1.shape
    for i in range(0, row ):
        mov_name = db_file1["Title"][i]
        mov_name = re.sub(r"b", "", mov_name)
        mov_name = re.sub(r"'", "", mov_name)
        mov_name = re.sub(r'"', '', mov_name)
        if name == mov_name or name == mov_name.lower():
            url = db_file1["Link"][i]
            break
    if url == "not found":
        for i in range(0, row + 1):
            mov_name = db_file1["AKA"][i]
            mov_name = re.sub(r"b", "", mov_name)
            mov_name = re.sub(r"'", "", mov_name)
            mov_name = re.sub(r'"', '', mov_name)
            if name == mov_name or name == mov_name.lower():
                url = db_file1["Link"][i]
                break
    print("url is ", url)
    return url


def imd_movie_db_create():
    ctr = 0
    val = file_check("imdb_movies.csv")
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
            movie_summary = get_imd_summary(movie_url)
            tmp_aka = aka(movie_url)
            clean_aka = tmp_aka
            clean_aka = re.sub(r"\n", "", clean_aka)
            clean_aka = re.sub(r" ", "", clean_aka)
            clean_aka = re.sub(r"\t", "", clean_aka)
            movie_aka = str(clean_aka.encode('utf-8'))
            movie_title = str(movie_title.encode('utf-8'))
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

    db_file1.close()


def reviews_db_create(name):
    ctr = 0
    val = file_check("movie_reviews.csv")
    if val:
        return
    else:
        db_file1 = open("movie_reviews.csv", "w", encoding='utf-8')
        db_file1.write("Comment,Reviews,UsrRating,TotalRating\n")

    url = get_mov_url(name)
    if url == "not found":
        return
    else:
        all_rev_url = get_mov_reviews(url)
        print(all_rev_url)
        if all_rev_url != "No Reviews found for this Movie":
            page = requests.get(all_rev_url)
            soup = BeautifulSoup(page.text, 'html.parser')
            tag1 = soup.find_all("a", class_="title")
            tag2 = soup.find_all("div", class_="text show-more__control")
            tag3 = soup.find_all("div", class_="ipl-ratings-bar")
            movie_comment, movie_review, movie_user_rating, tot_rating = "No Comment", "No Review", "No Rating", "10"
            num = min(len(tag1),len(tag2),len(tag3))
            for i in range(0, num):
                small_comment = tag1[i].text
                full_review = tag2[i].text
                subtag1 = tag3[i].find_all("span")
                imdb_user_rating = subtag1[len(subtag1) - 2].text
                total_rating = subtag1[len(subtag1) - 1].text
                movie_user_rating = imdb_user_rating
                tot_rating = total_rating
                movie_comment = re.sub(r"\n", "", small_comment)
                movie_review = re.sub(r"\n", "", full_review)
                #movie_review = re.sub(r"<.*?>","",full_review)
                movie_comment = re.sub(r",", "", movie_comment)
                movie_review = re.sub(r",", "", movie_review)
                movie_user_rating = re.sub(r"\n", "", movie_user_rating)
                print("\nMovie Comment ", movie_comment)
                print("\nMovie Review ", movie_review)
                print("\nUser Rating ", movie_user_rating)
                print("\nTotal Rating ", tot_rating)
                print("\nfine till here 10")
                db_file1.write(movie_comment)
                db_file1.write(",")
                db_file1.write(movie_review)
                db_file1.write(",")
                db_file1.write(movie_user_rating)
                db_file1.write(",")
                db_file1.write(tot_rating)
                db_file1.write("\n")
                ctr = ctr + 1
                if ctr == 50:
                    break
        else:
            db_file1.write(",")
            db_file1.write(all_rev_url)
            db_file1.write(",,")
            db_file1.write("\n")
        db_file1.close()


class Ui_sec_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(40, 10, 325, 231))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(100, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame2)
        self.progressBar.setGeometry(QtCore.QRect(40, 140, 290, 25))
        self.progressBar.setRange(0, 100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMovie_Rater_1_0 = QtWidgets.QAction(MainWindow)
        self.actionMovie_Rater_1_0.setObjectName("actionMovie_Rater_1_0")
        self.menuabout.addAction(self.actionMovie_Rater_1_0)
        self.menubar.addAction(self.menuabout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("About", "Movie Spice is a Movie Rater\nVersion 1.0"))
        self.inc_prog_bar()
        return self.progressBar.value()

    def inc_prog_bar(self):
        for i in range(0, 101):
            if i == 0:
                self.label.adjustSize()
            elif i % 2 == 0:
                self.label.setText("Loading Result /")
            else:
                self.label.setText("Loading Result \\")
            self.label.adjustSize()
            self.progressBar.setValue(i)
            QApplication.processEvents()
            time.sleep(0.5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Spice"))
        self.label.setText(_translate("MainWindow", "Loading result"))
        self.label.adjustSize()
        self.menuabout.setTitle(_translate("MainWindow", "About"))
        self.actionMovie_Rater_1_0.setText(_translate("MainWindow", "Movie Spice"))

    def show_popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if title == "Error":
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry)
        else:
            msg.setIcon(QMessageBox.Information)

        x = msg.exec_()


class Ui_third_Window(object):
    def setupUi(self, MainWindow, rat1: int, rat2: int, rat3: int, rat4: int):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(20, 20, 431, 301))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        if rat1 == 0 and rat2 == 0 and rat3 == 0 and rat4 == 0:
            self.label_2 = QtWidgets.QLabel(self.frame3)
            self.label_2.setGeometry(QtCore.QRect(110, 50, 47, 13))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.frame3)
            self.label_3.setGeometry(QtCore.QRect(50, 80, 47, 13))
            self.label_3.setObjectName("label_3")
        else:
            self.label_2 = QtWidgets.QLabel(self.frame3)
            self.label_2.setGeometry(QtCore.QRect(190, 50, 47, 13))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.frame3)
            self.label_3.setGeometry(QtCore.QRect(90, 80, 47, 13))
            self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame3)
        self.label_4.setGeometry(QtCore.QRect(90, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame3)
        self.label_5.setGeometry(QtCore.QRect(90, 140, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame3)
        self.label_6.setGeometry(QtCore.QRect(90, 170, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame3)
        self.label_7.setGeometry(QtCore.QRect(90, 200, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame3)
        self.label_8.setGeometry(QtCore.QRect(90, 240, 47, 13))
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_6.setFont(font)
        self.label_7.setFont(font)
        self.label_8.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMovie_Rater_1_0 = QtWidgets.QAction(MainWindow)
        self.actionMovie_Rater_1_0.setObjectName("actionMovie_Rater_1_0")
        self.menuabout.addAction(self.actionMovie_Rater_1_0)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow, rat1, rat2, rat3, rat4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("About", "Movie Spice is a Movie Rater\nVersion 1.0"))

    def retranslateUi(self, MainWindow, rat1: int, rat2: int, rat3: int, rat4: int):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Spice"))
        if rat1 == 0 and rat2 == 0 and rat3 == 0 and rat4 == 0:
            self.label_2.setText(_translate("MainWindow", "This is a Latest 2020 movie"))
            self.label_3.setText(_translate("MainWindow", "Therefore no movie reviews for it were found"))
        else:
            self.label_2.setText(_translate("MainWindow", "Movie Ratings"))
            self.label_3.setText(_translate("MainWindow", "Acting = " + str(rat1) + "/10"))
            self.label_4.setText(_translate("MainWindow", "Plot = " + str(rat2) + "/10"))
            self.label_5.setText(_translate("MainWindow", "Sound = " + str(rat3) + "/10"))
            self.label_6.setText(_translate("MainWindow", ""))
            self.label_7.setText(_translate("MainWindow", ""))
            self.label_8.setText(_translate("MainWindow", "Overall Rating = " + str(rat4) + "/10"))
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        self.label_8.adjustSize()
        self.menuabout.setTitle(_translate("MainWindow", "About"))
        self.actionMovie_Rater_1_0.setText(_translate("MainWindow", "Movie Spice"))

    def show_popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if title == "Error":
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry)
        else:
            msg.setIcon(QMessageBox.Information)

        x = msg.exec_()


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(464, 382)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("project_logo.png"),QtGui.QIcon.Selected,QtGui.QIcon.On)
        self.setWindowIcon(self.icon)
        self.sec_window = Ui_sec_Window()
        self.third_window = Ui_third_Window()
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(40, 40, 381, 261))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.mov_name = QtWidgets.QTextEdit(self.frame1)
        self.mov_name.setGeometry(QtCore.QRect(190, 80, 141, 21))
        self.mov_name.setObjectName("textEdit")
        self.ok_button = QtWidgets.QPushButton(self.frame1)
        self.ok_button.setGeometry(QtCore.QRect(270, 170, 91, 41))
        self.ok_button.setObjectName("ok_button")
        self.ques1 = QtWidgets.QLabel(self.frame1)
        self.ques1.setGeometry(QtCore.QRect(55, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ques1.setFont(font)
        self.ques1.setObjectName("ques1")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionMovie_Rater_1_0 = QtWidgets.QAction(self)
        self.actionMovie_Rater_1_0.setObjectName("actionMovie_Rater_1_0")
        self.menuabout.addAction(self.actionMovie_Rater_1_0)
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.actionMovie_Rater_1_0.triggered.connect(lambda: self.show_popup("About", "Movie Spice is a Movie Rater\nVersion 1.0"))
        self.ok_button.clicked.connect(self.on_click)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Movie Spice"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.ques1.setText(_translate("MainWindow", "Enter a Movie Name"))
        self.mov_name.setText(_translate("MainWindow", "Enter Text here"))
        self.menuabout.setTitle(_translate("MainWindow", "About"))
        self.actionMovie_Rater_1_0.setText(_translate("MainWindow", "Movie Spice"))

    def show_popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if title == "Error":
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry)
        else:
            msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

    def switch_to_third(self, rat1: int, rat2: int, rat3: int, rat4: int):
        self.third_window.setupUi(self, rat1, rat2, rat3, rat4)
        self.show()

    def switch_to_sec(self):
        progress = self.sec_window.setupUi(self)
        self.show()
        rat1, rat2, rat3, rat4 = calc_score()
        print("Fine till here 15 ")
        if progress == 100:
            self.switch_to_third(rat1, rat2, rat3, rat4)

    def on_click(self):
        movie_name = self.mov_name.toPlainText()
        print("fine till here 1")
        if movie_name == "Enter Text here":
            self.show_popup("Error", "You have not Entered a movie name.")
        elif check_mov(movie_name):
            reviews_db_create(movie_name)
            self.switch_to_sec()
        else:
            print("fine till here False")
            self.show_popup("Error", "The movie name is not valid.")


if __name__ == "__main__":
    # imd_movie_db_create()
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()

    ui.show()
    sys.exit(app.exec_())
