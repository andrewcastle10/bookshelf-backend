import requests, json
from urllib import request as ulreq
from PIL import ImageFile
import pandas as pd


def GetBookData(search_query):
    
    search_base = "http://openlibrary.org/search.json?q="

    url = search_base + search_query

    r = requests.get(url)

    data = json.loads(r.text)
    docs = data['docs']

    keys = []
    titles = []
    isbns = []

    for doc in docs:
        # print(doc)
        keys.append(doc['key'])
        titles.append(doc['title'])
        if 'isbn' in doc:
            isbns.append(doc['isbn'][0])
        else:
            isbns.append(None)

    # print(titles)
    return {'keys':keys, 'titles':titles, 'isbns':isbns}


def GetBookCovers(book_data):
    # print(book_data)
    urls_out = []
    keys_out = []
    titles_out = []

    for idx, key in enumerate(book_data['isbns']):
        if key is not None:
            url = "https://covers.openlibrary.org/b/isbn/" + key + "-L.jpg"
            url = FilterBadImages(url)

            if url is not None:
                urls_out.append(url)
                keys_out.append(book_data['isbns'][idx])
                titles_out.append(book_data['titles'][idx])

    return pd.DataFrame({'key':keys_out, 'title': titles_out, 'url':urls_out})


## Right now, some of the search results don't have a cover. This is a kind of hacky way to clean those out.
## Problem is, it's very slow and probably not scalable. Need to figure out a better solution here.
def FilterBadImages(uri):
    # get file size *and* image size (None if not known)
    file = ulreq.urlopen(uri)
    p = ImageFile.Parser()

    while True:
        data = file.read(10)
        if not data:
            break
        p.feed(data)
        if p.image:
            if p.image.size[0] > 1:
                file.close()
                return uri
            # return size, p.image.size
    file.close()
    return None

# https://covers.openlibrary.org/b/olid/OL7440033M-S.jpg
# https://covers.openlibrary.org/b/OLID/OL9084731W-L.jpg
# OL18642726M

# OL276558W