from DocumentProcessor import DocumentProcessor
from DocumentRepository import DocumentRepository


class DocumentController:

    @staticmethod
    def search(search):
        search = search.split(' ')
        search.append('0')

        pages = DocumentRepository.get_pages_from_word(search[0].lower(), search[1].lower())

        if len(pages) == 0:
            print("-> Não encontramos resultados para sua busca")
            return

        DocumentController.show_pages(pages)

    @staticmethod
    def show_pages(pages, limit=20):
        for key in list(pages.keys())[:limit]:
            print(f"{pages[key].title} {pages[key].count}")

    @staticmethod
    def load():
        DocumentProcessor.load("data/verbetesWikipedia.xml")
