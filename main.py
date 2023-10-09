import time

from DocumentController import DocumentController
from DocumentRepository import DocumentRepository

print("loading...")
start = time.time()

DocumentController.load()
DocumentRepository.show()

end = time.time()
print(f"time: {end - start}s")

while True:
    search = input("::: ")

    if not search:
        break

    DocumentController.search(search)