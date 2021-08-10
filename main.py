import redis
redis_host='localhost'
redis_port=6379
redis_password=""
def hello_redis():
    """Hello world redis program redis-cli to SET Bahmas shutdown"""
    try:
            #create a redis connection object
            r=redis.StrictRedis(host=redis_host,port=redis_port,password=redis_password,decode_responses=True)
            #set the hello world message
            r.set("msg:hello","Hello World!!")
            #Retrive the hello world messagde
            msg=r.get("msg:hello")
            print(msg)
    except Exception as e:
        print(e)
if __name__=='__main__':
    hello_redis()