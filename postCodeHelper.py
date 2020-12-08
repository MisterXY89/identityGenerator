
import requests
from bs4 import BeautifulSoup
from infoCrawler import requestAssistant as ra

class PostCodeHelper:
    def __init__(self):
        self.baseUrl = "https://worldpostalcode.com/lookup"
        self.rhg = ra.RequestHeaderGenerator()

    def getPostcode(self, city):
        print(city)
        try:
            print("inside try")
            req = requests.post(self.baseUrl, data={'val': city}, headers=self.rhg.getRandomRequestHeader())
            if int(req.status_code) == 200:
                return self._parseCode(req.content)
            else:
                print(req.status_code, req.reason)
        except:
            print(req.status_code, req.reason)

    def _getSoup(self, html_doc):
        return BeautifulSoup(html_doc, 'html.parser', from_encoding="utf-8")

    def _parseCode(self, html_doc):
        soup = self._getSoup(html_doc)
        print(soup)
        searchUnits = soup.find_all("div", class_="search_unit")
        print(searchUnits)
        for unit in searchUnits:
            country = unit.find_all("div")[0].text
            print(country)
        return 0


pch = PostCodeHelper()
pch.getPostcode("Berlin")
input()
