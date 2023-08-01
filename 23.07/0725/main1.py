# 접속

import redis


# 데이터베이스 접속
with redis.StrictRedis(host='localhost', port=6379) as conn :
    # 문자열 저장
    conn.set("name", "adam")
    # 문자열 가져오기 - bytes로 리턴
    data = conn.get("name")
    print(data) #인코딩 결과가 출력됨
    print(data.decode('utf-8')) # 디코딩


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