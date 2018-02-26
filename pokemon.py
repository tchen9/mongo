'''

Pokemon GO Pokedex

Description of Contents: All information relevant to the game, including id number, name, types, weaknesses, candy count, spawn chance, spawn time, etc.

Hyperlink: https://github.com/Biuni/PokemonGO-Pokedex/blob/master/pokedex.json

Import Mechanism: Imported using json.load(open(json file)) and then taking the value of key "pokemon," which happens to be all the data 

'''

import pymongo
import json

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection['Kanto']
collection = db['pokemon']

#commented out to prevent new documents every time program is run
#data = json.load(open('pokemon.json'))
#data = data['pokemon']
#for pokemon in data:
#    collection.insert(pokemon)

#find pokemon by name
def findName(name):
    pokemon = collection.find( {'name': name} )
    for each in pokemon:
        print each

#find pokemon by egg type
#possible parameters: "2 km", "5 km", "10 km", "Not in Eggs" 
def findEgg(egg):
    pokemon = collection.find( {'egg': egg} )
    for each in pokemon:
        print each

#find pokemon by candy count less than or equal to max value
def findCandyCount(maxVal):
    pokemon = collection.find( {'candy_count': {'$lte': maxVal}} )
    for each in pokemon:
        print each
        
#find pokemon by spawn chance between min and max values, inclusive
def findSpawn(minVal, maxVal):
    pokemon = collection.find( {'spawn_chance': {'$gte': minVal, '$lte': maxVal}} )
    for each in pokemon:
        print each
            
#find pokemon by primary type
def findType(type):
    pokemon = collection.find( {'type.0': type} )
    for each in pokemon:
        print each
        
#findName('Bulbasaur')
#findEgg('Not in Eggs')
#findCandyCount(20)
#findSpawn(0.4, 0.75)
findType("Water")
