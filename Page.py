class Page:
    def __init__(self, id: int, title: str, text: str):
        self.id = id
        self.title = title
        self.text = text
        self.count = 0

    def increment_count(self, value: float):
        self.count += value
