import xml.etree.ElementTree as ET
from operator import itemgetter

def count_word_in_text(word, text, count = 0):
    text = text.split()
    for s in text:
        if word.lower() in s.lower():
            count += 1
    return count

def print_result(results):
    results = sorted(results, key=itemgetter('occurences'), reverse=True) # order by occurences DESC

    f = open("result.txt", "w") 
    for page in results[0:20]:
        f.write(f'{page["title"]} {page["occurences"]}\n')
        print(f'{page["title"]} {page["occurences"]}\n')
    f.close()

tree = ET.parse("verbetesWikipedia.xml")
root = tree.getroot()

cache = {}
while(1):
    search = input("::: ")

    if search in cache: # exists in cache
        print_result(cache[search])
    else:
        cache[search] = []
        for page in root.findall('page'):
            title = page.find("title").text
            text = page.find("text").text

            occurences = count_word_in_text(search, text)
            if search.lower() in page.find('title').text.lower():
                occurences += 10
            
            cache[search].append({
                "title": title,
                "text": text,
                "occurences": occurences
            })

        print_result(cache[search])

    