
import requests
from bs4 import BeautifulSoup, SoupStrainer
from infoCrawler.requestAssistant import RequestHeaderGenerator


class BasicCrawler:
    """
    docstring for BasicCrawler.
    """

    def __init__(self):
        self.rhg = RequestHeaderGenerator()

    def get_soup(self, url):
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
