import json


data = {}

def loadData():
    with open('db') as db:
        data = db.read()
