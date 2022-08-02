import requests, json

search_base = "http://openlibrary.org/search.json?q="
q = 'the+lord+of+the+rings'


url = search_base + q

r = requests.get(url)
# print(r.text)


data = json.loads(r.text)
print(type(data))
print(len(data))
docs = data['docs']
for doc in docs:
    
    book_dat = [doc['key'], doc['title']]
    if 'author_name' in doc:
        book_dat.append(doc['author_name'])
    if 'isbn' in doc:
        book_dat.append(doc['isbn'])
    if 'publish_year' in doc:
        book_dat.append(doc['publish_year'])

    print(book_dat)