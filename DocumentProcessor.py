import xml.etree.ElementTree as ET

from Cache import Cache
from Page import Page

SCORE_TITLE = 10
SCORE_TEXT = 1


class DocumentProcessor:
    def __init__(self, src):
        self.root = ET.parse(src).getroot()
        self.cache = Cache()

    def load_words(self, ):
        for page in self.__get_pages():
            title = self.__get_title(page)
            text = self.__get_text(page)

            contents = [
                {
                    'content': title.lower().split(),
                    'score': SCORE_TITLE
                },
                {
                    'content': text.lower().split(),
                    'score': SCORE_TEXT
                }
            ]

            for c in contents:
                for word in c['content']:
                    self.process_word(word, title, text, c['score'])

        return

    def search(self, filter):
        pages = self.cache.get(filter.lower())

        if pages == 0:
            print("-> Não encontramos resultados para sua busca")
            return

        pages = self.sort_pages(pages)
        for key in list(pages.keys())[:20]:
            print(f"{pages[key].title} {pages[key].occurrences}")

    def process_word(self, word, title, text, score):
        if self.word_is_valid(word):
            page = self.cache.get(word, title)

            if not page:
                page = Page(title, text)
                
            page.increment_occurrence(score)

            self.cache.insert(word, title, page)

    def __get_pages(self):
        return self.root.findall('page')

    @staticmethod
    def __get_title(page):
        return page.find('title').text

    @staticmethod
    def __get_text(page):
        return page.find('text').text

    @staticmethod
    def word_is_valid(word):
        return len(word) > 3

    @staticmethod
    def sort_pages(pages, reverse=True):
        return {k: v for k, v in sorted(pages.items(), key=lambda item: item[1].occurrences, reverse=reverse)}
