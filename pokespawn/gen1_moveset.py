# gen1db.py

from bs4 import BeautifulSoup
import requests
import os
import re

def file_check():
	fcheck = os.path.isfile("C:/Users/Linux/Documents/pokespawn/gen1_lvlmoves.csv")
	return fcheck


url = 'https://pokemondb.net/pokedex/game/red-blue-yellow'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
gen1_pokemons = soup.find_all("div", class_ = "infocard game-red-blue")


def gen1_db_create():
	ctr = 0
	val = file_check()
	if val:
		db_file1 = open("gen1_lvlmoves.csv", "a")
	else:
		db_file1 = open("gen1_lvlmoves.csv", "w")
		for i in range(0,101):
			db_file1.write(str(i))
			if i != 100:
				db_file1.write(",")
			else:
				db_file1.write("\n")
	
	counter = 0
	for pokemon in gen1_pokemons:
		poke_url = 'https://pokemondb.net' + gen1_pokemons[counter].a['href']
		poke_page = requests.get(poke_url)
		poke_soup = BeautifulSoup(poke_page.text, 'html.parser')
		dex_num = poke_soup.td.strong.text
		poke_name = poke_soup.h1.text
		poke_abilities = poke_soup.find_all("span", class_ = "text-muted")
		no_of_abilities = len(poke_abilities)-3
		poke_ability1 = poke_abilities[0].a.text
		if no_of_abilities > 1 and poke_abilities[1].a.text != poke_name:
			poke_ability2 = poke_abilities[1].a.text
		else:
			poke_ability2 = ""
		if poke_soup.find("small", class_ = "text-muted").a is None:
			hidden_abilities = ""
		else:
			hidden_abilities = poke_soup.find("small", class_ = "text-muted").a.text
		
		base_stats = poke_soup.find_all("td", class_ = "cell-num")
		base_hp = base_stats[0].text
		base_attack = base_stats[3].text
		base_defense = base_stats[6].text
		base_sp_attack = base_stats[9].text
		base_sp_defense = base_stats[12].text
		base_speed = base_stats[15].text
		
		poke_types = poke_soup.p.find_all("a")
		no_of_types = len(poke_types)
		poke_type1 = poke_types[0].text
		if no_of_types > 1:
			poke_type2 = poke_types[1].text
		else:
			poke_type2 = ""
		
		final_gender = ""
		poke_gender = poke_soup.find_all("td")
		for gender in poke_gender:
			if gender.text == "Genderless":
				final_gender = "Genderless"
				break
		
		if final_gender == "":
			male_gender_percent = poke_soup.find("span", class_ = "text-blue").text
			female_gender_percent = poke_soup.find("span", class_ = "text-pink").text
		
		if counter == 28 or counter == 31:
			poke_name = poke_name[:-1]
		if poke_ability2 == "" and final_gender == "":
			db_file1.write(dex_num + "," + poke_name + "," + poke_ability1 + "/" + hidden_abilities + "," + base_hp + "," + base_attack + "," + base_defense + "," + base_sp_attack + "," + base_sp_defense + "," + base_speed + "," + poke_type1 + "," + poke_type2 + "," + male_gender_percent + "/" + female_gender_percent)
		elif hidden_abilities == "" and poke_ability2 != "" and final_gender == "":
			db_file1.write(dex_num + "," + poke_name + "," + poke_ability1 + "/" + poke_ability2 + "," + base_hp + "," + base_attack + "," + base_defense + "," + base_sp_attack + "," + base_sp_defense + "," + base_speed + "," + poke_type1 + "," + poke_type2 + "," + male_gender_percent + "/" + female_gender_percent)
		elif hidden_abilities == "" and poke_ability2 == "" and final_gender == "":
			db_file1.write(dex_num + "," + poke_name + "," + poke_ability1 + "," + base_hp + "," + base_attack + "," + base_defense + "," + base_sp_attack + "," + base_sp_defense + "," + base_speed + "," + poke_type1 + "," + poke_type2 + "," + male_gender_percent + "/" + female_gender_percent)
		elif final_gender == "":
			db_file1.write(dex_num + "," + poke_name + "," + poke_ability1 + "/" + poke_ability2 + "/" + hidden_abilities + "," + base_hp + "," + base_attack + "," + base_defense + "," + base_sp_attack + "," + base_sp_defense + "," + base_speed + "," + poke_type1 + "," + poke_type2 + "," + male_gender_percent + "/" + female_gender_percent)
		else:
			db_file1.write(dex_num + "," + poke_name + "," + poke_ability1 + "/" + poke_ability2 + "/" + hidden_abilities + "," + base_hp + "," + base_attack + "," + base_defense + "," + base_sp_attack + "," + base_sp_defense + "," + base_speed + "," + poke_type1 + "," + poke_type2 + "," + final_gender)
		db_file1.write("\n")
		counter = counter + 1

if __name__ == '__main__':
	gen1_db_create()