from DocumentRepository import DocumentRepository
from Page import Page
from Score import Score
from XMLDocument import XMLDocument


class DocumentProcessor:

    @staticmethod
    def load(src: str):
        root = XMLDocument(src)

        for page in root.get_pages():
            print(count)
            (id, title, text) = (root.get_id(page), root.get_title(page), root.get_text(page))

            contents = DocumentProcessor.create_contents(title, text)

            for c in contents:
                for word in c['content']:
                    DocumentProcessor.process_word(word.lower(), id, title, text, c['score'])

        return

    @staticmethod
    def process_word(word, id, title, text, score):
        if DocumentProcessor.__word_is_valid(word):
            page = DocumentRepository.get_page(word, id)

            if not page:
                page = Page(id, title, text)
            page.increment_count(score)

            DocumentRepository.insert(word, page)

    @staticmethod
    def create_contents(title, text):
        return [
                {
                    'content': title.lower().split(),
                    'score': Score.TITLE.value
                },
                {
                    'content': text.lower().split(),
                    'score': Score.TEXT.value
                }
            ]

    @staticmethod
    def __word_is_valid(word):
        return len(word) > 3


