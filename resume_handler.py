
import os
import pdfkit
from pyresparser import ResumeParser

from basic_crawler import BasicCrawler

class ResumeHandler(BasicCrawler):
    """
    docstring for ResumeHandler.
    """

    def __init__(self):
        super(ResumeHandler, self).__init__()
        self.resume_url = "https://fake.jsonresume.org/resume"
        # self.resume_url = "https://thisresumedoesnotexist.com/"


    def save_to_file(self, text):
        filename = "tmp/resume.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(text)
        return filename

    def get_resume(self):
        filename = "tmp/resume.pdf"
        # resume_text = self.get_soup(self.resume_url).text
        # return self.save_to_file(resume_text)
        pdfkit.from_url(self.resume_url, filename)
        return filename

    def get_data(self):
        file = self.get_resume()
        print(file)
        data = ResumeParser(file).get_extracted_data()
        return data

rh = ResumeHandler()
# rh.get_resume()
data = rh.get_data()
print(data)
