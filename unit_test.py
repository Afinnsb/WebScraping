import unittest
import main
import requests
from bs4 import BeautifulSoup

url = "https://www.koton.com/tr/kadin/giyim/elbise/c/M01-C02-N01-AK103?q=%3Arelevance&psize=192&page=0"
headers = {
        "User-agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.content, "html.parser")



class test_Scraping(unittest.TestCase):
    def test_prod_info(self):
        result=main.prod_info()
        self.assertEqual(len(result),int(soup.find("span",{"class":"plt-count"}).text[:-5].replace("(","").replace(".","").strip()))



if __name__=='__main__':
    unittest.main()