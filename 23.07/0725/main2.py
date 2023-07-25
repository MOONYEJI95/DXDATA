import redis
# Connection Pool을 이용한 접속
import time
redis_pool = redis.ConnectionPool(host='lacalhost', port=6379, max_connections=4)
with redis.StrictRedis(connection_pool=redis_pool) as conn:
    # 만료 시간 설정 가능
    conn.set("name", "adam", 10) # 만료시간이 10초
    # 만료시간 확인
    print(conn.ttl("name"))

    conn.set("song","노래")
    conn.expire("song",10) # 데이터의 만료시간을 10초로 설정
    print(conn.get("song"))
    time.sleep(20)
    print(conn.get("song")) # 20초 후에 데이터를 가져오므로 데이터가 없어서 None