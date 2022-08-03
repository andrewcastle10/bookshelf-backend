import requests, json
from DataGetters import GetBookData, GetBookCovers


data = GetBookData("guns germs and steel")

covers = GetBookCovers(data['keys'])

print(covers)
