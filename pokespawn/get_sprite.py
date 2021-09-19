from bs4 import BeautifulSoup
import requests

url = "https://pokemondb.net/sprites"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
tag = soup.find_all("a", class_ = "infocard") 
for i in range(151,896):
	poke_url = "https://pokemondb.net/" + tag[i]['href']
	img_page = requests.get(poke_url)
	img_soup = BeautifulSoup(img_page.text,'html.parser')
	img_tag = img_soup.find_all("span", class_ = "img-fixed img-sprite-v203")
	for j in range(0,len(img_tag)):
		img_url = img_tag[j]['data-src']
		img_data = requests.get(img_url)
		file_name = str(j) + img_url.split('/')[-1]
		sprite_file = open(file_name,"wb")
		sprite_file.write(img_data.content)
		sprite_file.close()

print("Done with Task")