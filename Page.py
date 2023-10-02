class Page:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.occurrences = 1

    def increment_occurrence(self, value):
        self.occurrences += value
