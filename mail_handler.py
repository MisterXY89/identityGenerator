
from bs4 import BeautifulSoup
from basic_crawler import BasicCrawler

class MailHandler(BasicCrawler):
    """
    10-minute mail python handler
    """

    def __init__(self):
        super(MailHandler, self).__init__()
        self.mail_url = "https://10minutemail.com/"
        self.mail_selector = "#mail_address"


    def _parse(self, soup):
        return soup.select(self.mail_selector)

    def get_mail(self):
        soup = self.get_soup(self.mail_url)
        mail = self._parse(soup)
        print(mail)
        print(mail["value"])
        return mail


mh = MailHandler()
mh.get_mail()
