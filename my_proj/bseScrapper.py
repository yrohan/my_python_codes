import re
import string
import urllib3

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

class CompaniesScrapper(object):
    def __init__(self):
        self.url = "http://www.bseindia.com/corporates/List_Scrips.aspx"
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1120, 550)

    def scrape(self):
        self.driver.get(self.url)

        market_segment = Select(self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddSegment'))
        market_segment.select_by_value('Equity')

        company_status = Select(self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStatus'))
        company_status.select_by_value('Active')

        self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSubmit').click()
        
        # file = open('companies.html','w')
        # file.write(page_html)
        # file.close()

        pageno = 2

        while True:
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            xxx = soup.findAll("table", {"id":"ctl00_ContentPlaceHolder1_gvData"})
            print(xxx)

            # pagination
            try:
                next_page_elem = self.driver.find_element_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_gvData']/tbody/tr[1]/td/table/tbody/tr/td/a[text()='%d']" % pageno)
            except NoSuchElementException:
                break #no more pages left

            print('page', pageno, '\n')
            next_page_elem.click()

            pageno += 1
            if(pageno == 4):
                break



        self.driver.quit()

if __name__ == '__main__':
    scraper = CompaniesScrapper()
    scraper.scrape()        
