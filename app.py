# https://covers.openlibrary.org/b/$key/$value-$size.jpg <<- API format for a book cover
# EG: https://covers.openlibrary.org/b/isbn/9780393317558-L.jpg
# Other OpenLibrary stuff:
# https://openlibrary.org/dev/docs/api/books
## They have a book search!! I'm in business.
# https://openlibrary.org/dev/docs/api/search

## ISBN search works like this and could be scraped:
# https://isbnsearch.org/search?s=guns%2C+germs%2C+and+steel
## But, their search isn't very good, and they have captchas...

## This API is not free, but looks solid:
# https://isbndb.com/apidocs/v2

## Could use the Goodreads search and just scrape the result:
# https://www.goodreads.com/search?utf8=%E2%9C%93&query=jared+diamond

## To build this, really need to figure out the Amazon APIs
# https://webservices.amazon.com/paapi5/documentation/search-items.html


from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return jsonify("My Message!", 201)


