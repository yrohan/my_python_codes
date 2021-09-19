# gen1db.py

from bs4 import BeautifulSoup
import requests
import os
import re

def file_check():
	fcheck = os.path.isfile("C:/Users/Linux/Documents/pokespawn/gen1_extrainfo.csv")
	return fcheck


url = 'https://pokemondb.net/pokedex/game/red-blue-yellow'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
gen1_pokemons = soup.find_all("div", class_ = "infocard game-red-blue")


def gen1_db_create():
	ctr = 0
	val = file_check()
	if val:
		db_file1 = open("gen1_extrainfo.csv", "a")
	else:
		db_file1 = open("gen1_extrainfo.csv", "w")
		db_file1.write("Pokedex,PokeName,Exp,Friendship,GrowthRate,EvoLvl1,EvoLvl2,EvoStage1,EvoStage2,EvoStage3,EvoMethod1,EvoMethod2\n")
	
	counter = 0
	for pokemon in gen1_pokemons:
		poke_url = 'https://pokemondb.net' + gen1_pokemons[counter].a['href']
		poke_page = requests.get(poke_url)
		poke_soup = BeautifulSoup(poke_page.text, 'html.parser')
		dex_num = poke_soup.td.strong.text
		poke_name = poke_soup.h1.text
		tables = poke_soup.find_all("table", class_ = "vitals-table")
		table1 = tables[1]
		tag1 = table1.find_all("td")
		friendship = tag1[2].contents[0]
		base_exp = tag1[3].contents[0]
		growth_rate = tag1[4].contents[0]
		print(counter)
		'''print("Friendship = ",friendship)
		print("Base Exp = ",base_exp)
		print("Growth Rate = ",growth_rate)'''
		evo_lvl = []
		evo_methods = []
		evo_lvl1 = "none"
		evo_lvl2 = "none"
		evo_stage1 = "none"
		evo_stage2 = "none"
		evo_stage3 = "none"
		evo_method1 = "none"
		evo_method2 = "none"
		has_evo = poke_soup.find_all("span", class_ = "infocard infocard-arrow")
		if has_evo:
			for i in range(0,len(has_evo)):
				evo_lvls = has_evo[i].find("small")
				evo_lvl.append(evo_lvls.text)
				if has_evo[i].a:
					evo_methods.append(has_evo[i].a.text)
			
			evo_names = poke_soup.find_all("span", class_ = "infocard-lg-data text-muted")
			evo_stage1 = evo_names[0].a.text
			evo_stage2 = evo_names[1].a.text
			if len(evo_names) > 2:
				evo_stage3 = evo_names[2].a.text
			
		
		if evo_lvl:
			evo_lvl1 = evo_lvl[0]
			evo_lvl1 = evo_lvl1[7:-1]
			if len(evo_lvl) > 1:
				evo_lvl2 = evo_lvl[1]
				evo_lvl2 = evo_lvl2[7:-1]
		if evo_methods:
			evo_method1 = evo_methods[0]
			if len(evo_methods) > 1:
				evo_method2 = evo_methods[1]
		'''print("Evolution Level1 = ", evo_lvl1)
		print("Evolution Level2 = ", evo_lvl2)
		print("Evolution Stage1 = ", evo_stage1)
		print("Evolution Stage2 = ", evo_stage2)
		print("Evolution Stage3 = ", evo_stage3)
		print("Evolution Method = ", evo_method)
		
		print("\n")'''
		print(evo_lvl)
		print(evo_methods)
		if counter == 28 or counter == 31:
			poke_name = poke_name[:-1]
		
		if counter in range(28,34):
			evo_stage1 = evo_stage1[:-1]
		
		db_file1.write(dex_num + "," + poke_name + "," + base_exp + "," + friendship + "," +  growth_rate + "," +  evo_lvl1 + "," + evo_lvl2 + "," + evo_stage1 + "," + evo_stage2 + "," + evo_stage3 + "," + evo_method1 + "," + evo_method2)
		db_file1.write("\n")
		counter = counter + 1
	db_file1.close()

if __name__ == '__main__':
	gen1_db_create()
	print("Excution was successful")