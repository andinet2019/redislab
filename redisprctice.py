import redis
import datetime
local_host='localhost'
redis_port=6379
redis_password=""
r=redis.StrictRedis(host=local_host,port=redis_port,password=redis_password)
today=datetime.date.today()
stoday=today.isoformat()
visitors = {"dan", "jon", "alex"}
r.sadd(stoday,*visitors)
print(r.smembers(stoday))
print(stoday)