import xml.etree.ElementTree as ET


class XMLDocument:
    def __init__(self, src):
        self.root = ET.parse(src).getroot()

    def get_pages(self):
        return self.root.findall('page')

    @staticmethod
    def get_id(page):
        return int(page.find('id').text)

    @staticmethod
    def get_title(page):
        return page.find('title').text

    @staticmethod
    def get_text(page):
        return page.find('text').text
