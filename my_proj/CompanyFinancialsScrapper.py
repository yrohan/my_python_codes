from urllib.request import urlopen
from bs4 import BeautifulSoup 

class CompanyFinancialsScrapper:

	def __init__(self, bse_code):
		self.url = "https://www.bseindia.com/stock-share-price/stockreach_financials.aspx?scripcode="+ str(bse_code) + "&expandable=0"

	def getQuarterlyResults(self, page_soup):
		soup = page_soup.find(id="ctl00_ContentPlaceHolder1_quatre")
		table_soup = soup.find(id="m").find("table")
		# file = open('quarter_results_in_million.html','w')
		# file.write(str(table_soup))
		# file.close()
		quarterly_data = []
		table_rows = table_soup.find_all("tr")
		for rp in range(0,len(table_rows)-3): #rp is the quarter row pointer. cp is the column pointer
			table_columns = table_rows[rp].find_all("td")
			if(rp==0):
				for cp in range(1, len(table_columns)-1):
					quarterly_data.append({"quarter" : table_columns[cp].text})
				continue
			if(rp==1):
				continue
			for cp in range(1,len(table_columns)-1):
				quarter = quarterly_data[cp-1]
				attribute_string = self.make_string_json_compatible(table_columns[0].text)
				quarter[attribute_string] = table_columns[cp].text
		return quarterly_data

	def getAnnualResults(self, page_soup):
		soup = page_soup.find(id="ctl00_ContentPlaceHolder1_anntre")
		table_soup = soup.find(id="am").find("table")
		# file = open('annual_results_in_million.html', 'w')
		# file.write(table_soup.prettify())
		# file.close()
		annual_data = []
		table_rows = table_soup.find_all("tr")
		for rp in range(0,len(table_rows)-3): #rp is the annual row pointer. cp is the column pointer
			table_columns = table_rows[rp].find_all("td")
			if(rp==0): #first row has the headers for all the years 
				for cp in range(1, len(table_columns)):
					annual_data.append({"year" : table_columns[cp].text})
				continue
			if(rp==1): #skip the second row. because its completely useless.
				continue
			for cp in range(1,len(table_columns)):
				year = annual_data[cp-1] #year contains a dictionary
				attribute_string = self.make_string_json_compatible(table_columns[0].text)
				year[attribute_string] = table_columns[cp].text
		return annual_data

	def make_string_json_compatible(self, s):
		s = s.lower()
		s = s.strip()
		s = s.replace(' ', '_')
		s = s.replace('%', 'percent')
		return s

	def scrape(self):
		uClient = urlopen(self.url)
		page_html = uClient.read()
		uClient.close()
		page_soup = BeautifulSoup(page_html, "html5lib")
		quarterly_data = self.getQuarterlyResults(page_soup)
		# print(quarterly_data)

		print("\n")
		print("\n")

		annual_data = self.getAnnualResults(page_soup)
		# print(annual_data)

		return [quarterly_data, annual_data]



if __name__ == '__main__':
	scraper = CompanyFinancialsScrapper(500002)
	print(scraper.scrape())	