from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def generate_html_page():
    path = "C:/Users/Linux/drivers/chromedriver.exe"
    driver = webdriver.Chrome(path)
    res_file = open("search_result.txt", "w")
    txt_searched = open("search_term.txt", "w")

    driver.get("http://www.imdb.com/chart/top")
    print(driver.title)

    search = driver.find_element_by_id("suggestion-search")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        article = main.find_element_by_class_name("article")
        header = main.find_element_by_class_name("findSearchTerm")
        tmp_res = article.text
        tmp_txt = header.text
        res_file.write(tmp_res)
        txt_searched.write(tmp_txt)
    except:
        driver.quit()

    res_file.close()
    txt_searched.close()
    time.sleep(20)
    driver.quit()


if __name__ == '__main__':
    generate_html_page()
    print("\nExecution was successfull")
