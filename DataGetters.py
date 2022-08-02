import requests, json


def GetBookData(search_query):
    
    search_base = "http://openlibrary.org/search.json?q="

    url = search_base + search_query

    r = requests.get(url)

    data = json.loads(r.text)
    docs = data['docs']

    keys = []
    titles = []
    
    for doc in docs:
        keys.append(doc['key'])
        titles.append(doc['title'])

    return {'keys':keys, 'titles':titles}


def GetBookCovers(keys):
    urls = ["https://covers.openlibrary.org/b/ID" + key + "-L.jpg" for key in keys]
    return url
