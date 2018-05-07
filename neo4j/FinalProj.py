
######
### RUN IN PYTHON 3
### Tomer Zwi tz2247
#####


from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "test"))

# def create_User(cls, tx, name):
# 	tx.run("CREATE (:User {name: $name})", name=name)

# def create_person(cls, tx, name):
#     tx.run("CREATE (:Person {name: $name})", name=name)


#############################
## Define Object/nodes
##############################

def add_user(name):
    with driver.session() as session:
        session.run("CREATE (n:User {name: $name})", name=name)

def add_photo(caption,uniqid):
    with driver.session() as session:
        session.run("CREATE (n:Photo {caption: $caption, uniqid: $uniqid})", caption=caption ,uniqid=uniqid)

def add_video(caption,uniqid):
    with driver.session() as session:
        session.run("CREATE (n:Video {caption: $caption, uniqid: $uniqid})", caption=caption ,uniqid=uniqid)
def add_story(name, numberphto, uniqid):
    with driver.session() as session:
        session.run("CREATE (n:Story {name: $name, numberphto: $numberphto ,uniqid: $uniqid})", name=name, numberphto=numberphto, uniqid=uniqid)
def add_comment(description,uniqid):
    with driver.session() as session:
        session.run("CREATE (n:Comment {description: $description, uniqid: $uniqid})", description=description,uniqid=uniqid)
def add_messg(content,uniqid):
    with driver.session() as session:
        session.run("CREATE (n:Messg {content: $content, uniqid: $uniqid})", content=content,uniqid=uniqid)
def add_history(name,uniqid):
    with driver.session() as session:
        session.run("CREATE (n:History {name: $name, uniqid: $uniqid})", name=name ,uniqid=uniqid)
def add_hashtag(caption,uniqid):
    with driver.session() as session:
        session.run("CREATE (n:Hashtag {caption: $caption, uniqid: $uniqid})", caption=caption,uniqid=uniqid)


###############
## Define relationship
#################

def detel():
	with driver.session() as session:
		with session.begin_transaction() as tx:
			tx.run("MATCH (n) DETACH DELETE n ")
	# print("delete")

# def create_follow(name_a, name_b):
#     with driver.session() as session:
#         with session.begin_transaction() as tx:
#         	for record in tx.run("MATCH (a:User),(b:User) "
#         	 	   "WHERE a.name = $name_a AND b.name = $name_b " 
#         	 	   "CREATE (a)-[r: Follow]->(b) " "RETURN type(r) ",name_a=name_a, name_b=name_b):
        		   
#            	    print(record["type(r)"])

def create_follow(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:User) "
        	 	   "WHERE a.name = $name_a AND b.name = $name_b " 
        	 	   "CREATE (a)-[r: Follow]->(b) " ,name_a=name_a, name_b=name_b)
        		   


# def create_likes(name_a, name_b):
#     with driver.session() as session:
#         with session.begin_transaction() as tx:
#         	for record in tx.run("MATCH (a:User),(b:Photo) "
#         	 	   "WHERE a.name = $name_a AND b.uniqid = $name_b " 
#         	 	   "CREATE (a)-[r: Likes]->(b) " "RETURN type(r) ",name_a=name_a, name_b=name_b):
        		   
#            	    print(record["type(r)"])


def create_likes(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:Photo) "
        	 	   "WHERE a.name = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: Likes]->(b) " ,name_a=name_a, name_b=name_b)
        		   

def create_comments(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:Comment),(b:Photo) "
        	 	   "WHERE a.uniqid = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: Belongto]->(b) ",name_a=name_a, name_b=name_b)
        		   

def create_commentsVid(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:Comment),(b:Video) "
        	 	   "WHERE a.uniqid = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: Belongto]->(b) ",name_a=name_a, name_b=name_b)


def create_getmess(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:User) "
        	 	   "WHERE a.name = $name_a AND b.name = $name_b " 
        	 	   "CREATE (a)-[r: getmessg]->(b) ",name_a=name_a, name_b=name_b)


def create_sentto(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:User) "
        	 	   "WHERE a.name = $name_a AND b.name = $name_b " 
        	 	   "CREATE (a)-[r: sentmess]->(b) ",name_a=name_a, name_b=name_b)


def create_hashtagPhoto(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:Hashtag),(b:Photo) "
        	 	   "WHERE a.uniqid = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: related]->(b) ",name_a=name_a, name_b=name_b)

def create_updatePhoto(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:Photo) "
        	 	   "WHERE a.name = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: updatephot]->(b) ",name_a=name_a, name_b=name_b)



def create_updateVido(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:Video) "
        	 	   "WHERE a.name = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: updatevide]->(b) ",name_a=name_a, name_b=name_b)


def create_History(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:Story),(b:History) "
        	 	   "WHERE a.uniqid = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: Located]->(b) ",name_a=name_a, name_b=name_b)


def create_story(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:Story) "
        	 	   "WHERE a.name = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: createSto]->(b) ",name_a=name_a, name_b=name_b)



def craete_wasATstory(name_a, name_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
        	tx.run("MATCH (a:User),(b:Story) "
        	 	   "WHERE a.name = $name_a AND b.uniqid = $name_b " 
        	 	   "CREATE (a)-[r: wasat]->(b) ",name_a=name_a, name_b=name_b)






########
### Define ACTINOS
##########

## who follow Joey

def Who_follow(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (f)-[:Follow]->(a:User) "
                                 #"WHERE a.name = {name} "
                                 "WHERE a.name = $name "
                                 "RETURN f.name", name=name):
                #print(record["f.name"])
                print(record["f.name"])


## who Adam follow 

def Follower(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:User)-[:Follow]->(f) "
                                 "WHERE a.name = {name} "
                                 "RETURN f.name", name=name):
                print(record["f.name"])


# name all the people who particpate in any story from the users
def Participate():
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a)-[r:wasat]->(b) " 
            	#"WHERE type(r)= wasat "
            	"RETURN a.name, type(r) "):
            	print(record["a.name"])

## list all the people who sent message thorugh the app
def Messg1():
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a)-[r:sentmess]->(b) " 
            	#"WHERE type(r)= wasat "
            	"RETURN a.name, type(r) "):
            	print(record["a.name"])


## 5 who update photo 1

def update_photo1(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (f)-[:updatephot]->(a:Photo) "
                                 "WHERE a.uniqid = {name} "
                                 "RETURN f.name", name=name):
                print(record["f.name"])



## 6 print who update video




## 7which comment belong to photo3

def comment_bleong(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (f)-[:Belongto]->(a:Photo) "
                                 "WHERE a.uniqid = {name} "
                                 "RETURN f.description", name=name):
                print(record["f.description"])






## contents of all the messge Joey got  message Joey got

def HistoryDate(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a)-[r:Located]->(b: History) "
                                 "WHERE b.name = {name} "
                                 "RETURN a.numberphto", name=name):
                print(record["a.numberphto"])
                #print(record)



def hastaga(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a)-[r:related]->(b: Photo) "
                                 "WHERE b.uniqid = {name} "
                                 "RETURN a.caption", name=name):
                print(record["a.caption"])




### list all the users that likes photo 3

def LikePh(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a)-[r:Likes]->(b: Photo) "
                                 "WHERE b.uniqid = {name} "
                                 "RETURN a.name", name=name):
                print(record["a.name"])


############
### Create Nodes
###############
detel()
add_user("Joey")
add_user("Judy")
add_user("Adam")
add_photo("Breakfest in new york","1")
add_photo("La_familia","2")
add_photo("TheGoodfriends","3")
add_comment("Look_amazing!!","4")
add_comment("Have Fun!!","5")
add_comment("WOOOOOOOOOWWWWW!!","6")
add_hashtag("I<3NY","7")
add_hashtag("Fun","8")
#add_hashtag("Wooow","16")
add_video("Massi's goal","9")
add_video("Night_in_Paris","10")
add_messg("How you doing, your last photos looks amazing","11")
add_history("May 2", "12")
add_history("May 2", "13")
add_story("May 1","3", "14")
add_story("May 2","9","15")






###############
## create relationship 
###############
create_follow ("Joey","Judy")
create_follow("Adam","Joey")
create_follow("Judy","Joey")
create_follow("Judy","Adam")
create_likes("Joey", "1")
create_likes("Joey", "2")
create_likes("Judy", "3")
create_likes("Adam", "3")
create_comments("4","2")
create_comments("5","3")
create_comments("6","1")
create_commentsVid("6","9")
create_getmess("Adam","Judy")
create_sentto("Judy","Adam")
create_hashtagPhoto("7","1")
create_hashtagPhoto("8","2")
create_updateVido("Judy","10")
create_updatePhoto("Adam","2")
create_updatePhoto("Joey","1")
create_History("15","12")
create_History("14","13")
create_story("Joey","14")
craete_wasATstory("Adam","14")



###################
#### Create Actions
##################

print("ACTIONS:::")

## action 1
print("List of all followers of Joey:")
Who_follow("Joey")

print(" ")

###  action 2
print("List of all the people who Adam following:")
Follower("Adam")

print(" ")


### action 3
print("name all the people who particpate in any story from the users:")
Participate()


print(" ")

### action 4
print( " who update photo 1:")
update_photo1("1")

print(" ")

### action 5
print("print the comment for photo 3:")
comment_bleong("3")

print(" ")

## action 6
print("all the user who likes photo 3:")
LikePh("3")


print(" ")

### action 7
print("print all the hashtag of photo 2:")
hastaga("2")

print(" ")
#### action 8
print("list all the people who sent message thorugh the app:")
Messg1()

## action 9
print(" ")

print("List all the amount of photos per story that has in May 12:")
HistoryDate("May 2")

