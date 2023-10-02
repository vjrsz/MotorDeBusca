from DocumentProcessor import DocumentProcessor

print("loading...")

processor = DocumentProcessor("./data/verbetesWikipedia.xml")
processor.load_words()

while True:
    search = input("::: ")

    if not search:
        break

    processor.search(search)
