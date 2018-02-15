import pymongo

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection['test']
collection = db['restaurants']

def findInBorough(borough):
    rests = collection.find({'borough' : borough})
    for rest in rests:
        print rest
        print '\n'
    
findInBorough('Bronx')

def findInZip(zip):
    rests = collection.find({'address.zipcode' : zip})
    for rest in rests:
        print rest
        print '\n'

findInZip('10460')

def findInZipGrade(zip, grade):
    rests = collection.find({'address.zipcode' : zip, 'grades.grade' : grade})
    for rest in rests:
        print rest
        print '\n'

findInZipGrade('10460', 'B')

def findInZipScore(zip, score):
    rests = collection.find({'address.zipcode' : zip, 'grades.score' : {"$gte" : score}})
    for rest in rests:
        print rest
        print '\n'

findInZipScore('10460', 15)
