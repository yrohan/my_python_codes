import re
import string
import urllib3
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

my_url=[]
m=["jet+airways","aegis+logistics"]
for i in range(0,len(m)):
    my_url+="https://in.reuters.com/search/news?blob="+m[i]



