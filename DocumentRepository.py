from collections import defaultdict
import networkx as nx


class DocumentRepository:
    _database = nx.Graph()
    _last_word = None

    @staticmethod
    def insert(word, page):
        DocumentRepository.insert_word(word)
        DocumentRepository.insert_page(word, page)

        if DocumentRepository._last_word:
            DocumentRepository.insert_relationship(word, DocumentRepository._last_word, page)
        DocumentRepository._last_word = word

    @staticmethod
    def insert_relationship(word1, word2, page):
        if not DocumentRepository.exist_relationship(word1, word2):
            DocumentRepository._database.add_edge(word1, word2, pages=defaultdict(lambda: 0))

        DocumentRepository._database[word1][word2]['pages'][page.id] = page

    @staticmethod
    def get_relationship(word1, word2):
        if DocumentRepository.exist_word(word1) and DocumentRepository.exist_word(word2):
            return DocumentRepository._database[word1][word2]
        return None

    @staticmethod
    def insert_word(word):
        if not DocumentRepository.exist_word(word):
            DocumentRepository._database.add_node(word, pages=defaultdict(lambda: 0))

    @staticmethod
    def get_word(word):
        if DocumentRepository.exist_word(word):
            return DocumentRepository._database.nodes[word]
        return None

    @staticmethod
    def insert_page(word, page):
        if DocumentRepository.exist_word(word):
            DocumentRepository._database.nodes[word]['pages'][page.id] = page

    @staticmethod
    def get_page(word, id):
        if DocumentRepository.exist_word(word):
            return DocumentRepository._database.nodes[word]['pages'][id]

    @staticmethod
    def get_pages_from_word(word1, word2):

        _word1 = DocumentRepository.get_word(word1)
        _word2 = DocumentRepository.get_word(word2)
        _word3 = DocumentRepository.get_relationship(word1, word2)

        if _word3:
            return DocumentRepository.sort_pages(_word3['pages'])
        elif _word2:
            return DocumentRepository.sort_pages(_word2['pages'])
        elif _word1:
            return DocumentRepository.sort_pages(_word1['pages'])
        else:
            return defaultdict(lambda: 0)

    @staticmethod
    def exist_word(word):
        return DocumentRepository._database.has_node(word)

    @staticmethod
    def exist_relationship(word1, word2):
        return DocumentRepository._database.has_edge(word1, word2)

    @staticmethod
    def sort_pages(pages):
        return defaultdict(lambda: 0, {k: v for k, v in sorted(pages.items(), key=lambda item: item[1].count, reverse=True)})

    @staticmethod
    def show():
        print(f"{len(DocumentRepository._database.nodes())} items")
