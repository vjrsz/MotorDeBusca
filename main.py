import time

from DocumentProcessor import DocumentProcessor

print("loading...")
start = time.time()

processor = DocumentProcessor("./data/verbetesWikipedia.xml")
processor.load_words()

end = time.time()
print(f"{end - start}s ...")

while True:
    search = input("::: ")

    if not search:
        break

    processor.search(search)
