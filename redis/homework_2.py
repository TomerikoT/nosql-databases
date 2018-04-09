import redis

import datetime
import json
import urllib.request


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(redis, user, article):
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)

    if not datetime.datetime.fromtimestamp(redis.zscore('time:', article)) < cutoff:
        article_id = article.split(':')[-1]
        if redis.sadd('voted:' + article_id, user):
            redis.zincrby(name='score:', value=article, amount=VOTE_SCORE)
            redis.hincrby(name=article, key='votes', amount=1)

def article_switch_vote(redis, user, from_article, to_article):
	from_id1 = from_article.split(':')[-1]
	to_id1 = to_article.split(':')[-1]
	#print(to_id1)
	#print (redis.smove('voted:' + from_id1, 'voted:' + to_id1, user))
	if redis.smove('voted:' + from_id1 ,'voted:'+ to_id1 ,user):
		#redis.sadd('voted:' + to_id1, user)
		redis.zincrby(name='score:', value = to_article, amount = 432)
		redis.hincrby(name=to_article, key ='votes', amount=1)

		#redis.sadd('voted:' + from_id1, user)
		redis.zincrby(name='score:', value=from_article, amount= -432)
		redis.hincrby(name=from_article, key='votes', amount=-1)
		#print("bla")
	else:
		pass;




redis = redis.StrictRedis(host='localhost', port=6379, db=0)
# user:3 up votes article:1
article_vote(redis, "user:3", "article:1")
# user:3 up votes article:3
article_vote(redis, "user:3", "article:3")
# user:2 switches their vote from article:8 to article:1
article_switch_vote(redis, "user:2", "article:8", "article:1")

x = redis.zrangebyscore('score:', 10, 20, start=None, num=None,withscores=False, score_cast_func=float) 
#print(x[0].decode('ascii'))
str = x[0].decode('ascii')
#print(redis.hget(str, "link"))

data = redis.hget(str,"link")
answer = "".join([chr(a) for a in data])

print (answer)


# PRINT THE ARTICLE'S LINK TO STDOUT:
# HOMEWORK 2 Part II
# article = redis.?
# print redis.?

