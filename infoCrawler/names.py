
import pickle
import requests
from os.path import join, dirname
from bs4 import BeautifulSoup, SoupStrainer
from requestAssistant import RequestHeaderGenerator

class Names:
    def __init__(self):
        self.baseUrl = "https://www.beliebte-vornamen.de/jahrgang/j"
        self.rhg = RequestHeaderGenerator()
        self.nameTableSelector = "inside-hitliste"
        self.namesDict = {}
        self.yearRange = range(1930, 2001)
        self.storeFile = join(dirname(__file__), 'files/names.pkl')

    def _getSoup(self, year):
        url = self.baseUrl + str(year)
        try:
            response = requests.get(url, headers = self.rhg.getRandomRequestHeader())
        except Exception as err:
            print(f"Error: {err}")
            return False
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")
            print(f"OK! Url: {url}")
            return soup
        else:
            print(f'Something went wrong. Got the following response code: {response.status_code}')
            return None

    def _prepNames(self, col):
        names = col.text.split()
        while "/" in names:
            index = names.index("/")
            del names[index:index+2]
        return names

    def _parse(self, soup):
        nameTable = soup.findAll("div", class_ = self.nameTableSelector)[0]
        cols = nameTable.findAll("td")
        names = {
            "girls": self._prepNames(cols[0]),
            "boys" : self._prepNames(cols[1])
        }
        return names

    def crawl(self, year):
        res = 0
        soup = self._getSoup(year)
        if soup != None:
            res = {str(year): self._parse(soup)}
        return res

    def _storeNames(self, obj):
        pickle.dump( obj, open( self.storeFile, "wb" ) )
        print("stored!")

    def crawlRange(self):
        for year in self.yearRange:
            self.namesDict.update(self.crawl(year))
        self._storeNames(self.namesDict)


n = Names()
n.crawlRange()
input()
