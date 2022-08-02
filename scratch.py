import requests, json


def GetBookData(search_query):
    
    search_base = "http://openlibrary.org/search.json?q="

    url = search_base + search_query

    r = requests.get(url)

    data = json.loads(r.text)
    docs = data['docs']
    
    for doc in docs:
        book_dat = [doc['key'], doc['title']]
        if 'author_name' in doc:
            book_dat.append(doc['author_name'])
        # if 'isbn' in doc:
        #     book_dat.append(doc['isbn'])
        # if 'publish_year' in doc:
        #     book_dat.append(doc['publish_year'])
        
        return book_dat

    return book_dat


def GetBookCover(key):
    url = "https://covers.openlibrary.org/b/ID" + key + "-L.jpg"
    return url
