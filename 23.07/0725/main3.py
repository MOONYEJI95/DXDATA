import redis
with redis.StrictRedis(host='localhost', port=6379) as conn :
    # 리스트에 데이터 저장
    conn.lpush("album","genesis")
    conn.rpush("album","exodus")

    for album in conn.lrange("album",0,10):
        print(album)