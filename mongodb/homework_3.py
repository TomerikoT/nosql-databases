import pymongo
from pymongo import MongoClient
import pprint
client = MongoClient()
#database = client.store
database = client.imdb1
collection = database.movies
#collection.find({"items.fruit": "banana"}).count()

#collection.find_and_modify(query={}, update=True, fields = { "rated.NOT RATED " : "rated.Pending rating" } )

## part a

collection.update_many({"genres":"Drama" } , {'$set' : {'rated' : 'Pending rating'} } )



## part b

collection.insert(
{
	
 "title" : "A Quiet Place ",
 "year" : 2018,
  "countries" : ["USA"], 
  "genres" : [ "Drama" , "Horror", "Sci-Fi"],
  "directors" : ["John Krasinski"],
  "imdb" : {'votes': 48227 , 'id':20 , 'rating':8.1}

}


)
#print ( collection.find({'title' : 'A Quiet Place' } )[0] )
#cursor = collection.find({'genres':'Drama'})
#for d in cursor :
 #   pprint.pprint(d)


# part c
p = collection.aggregate([  {'$unwind' : '$genres' } , { '$match' : {"genres" : "Drama"} }, {'$group': {"_id": "Drama", "count": {"$sum": 1}} }   ] )
#for x in p:
#    priint(x)


#p = collection.aggregate([ {'$match': {"country" : "Hungary"}, {"rating": "Pending rating"} } ,   {'$group': {"_id": {"country" : "Hungary" , "rating" : "Pending rating"}, "count": {"$sum": 1 } }} ] )

#p = collection.aggregate([ {'$match': "country" : "Hungary", "rating": "Pending rating" } ,   {'$group': {"_id": {"country" : "Hungary" , "rating" : "Pending rating"}, "count": {"$sum": 1 } }} ] )

# part d
ap = collection.aggregate(  [ {'$match': {"countries" : "Israel", "rated": "Pending rating" }}, {'$group': {"_id": { "country" : "Israel" , "rating" : "Pending rating"}, "count": {"$sum": 1 } }} ] )


# part e

database.actortv.insert([ { "name" : "Jenifer Asthon", "playat" : "friends"}, { "name": "Ryan gosling", "playat" : "veep"}, { "name":"emma stone", "playat" : "oc"}, { "name": "will smith", "playat" :"friends" } ] )

database.tvtvtv.insert([ { "tvname": "friend", "location": "los angeles"},
{ "tvname": "veep" , "location": "new york"}, { "tvname" :"mad man", "location":"dc"} ])


pa = database.actortv.aggregate([
   {
     '$lookup':
       {
         'from': "tvtvtv",
         'localField': "playat",
         'foreignField': "tvname",
         'as': "alistofactor"
       }
  }
])

for op in pa:

   print(op)

