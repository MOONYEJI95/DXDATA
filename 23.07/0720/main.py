<<<<<<< HEAD
import sys
import pymysql
try :
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='yeji', user='yeji', passwd='moon', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    # SQL 실행 - 값을 직접 SQL에 작성
    #cursor.execute("INSERT INTO DEPT VALUES(11,'비서','신안')")
    # SQL 실행 - SQL에 서식을 설정하고 파라미터를 대입하는 코드 작성
    # 12번 데이터의 부서를 영업 그리고 위치를 서초로 수정
    #cursor.execute("UPDATE DEPT SET DNAME = %s, LOC = %s WHERE DEPTNO = %s", ('영업','서초',12))
    # 12번 데이터 삭제
    #cursor.execute("DELETE FROM DEPT WHERE DEPTNO = %s", (12))

    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO > %s", (100))
    # 검색 된 결과가 없으면 None이고 존재하면 Tuple
    record = cursor.fetchone()
    if record == None :
        print("검색된 데이터가 없음")
    else :
        for attr in record :
            print(attr)
    # 검색 결과 전체 데이터를 읽어오는 것
    # 여러 개의 데이터를 가져오는 경우는 데이터가 없는 경우 빈 튜플을 리턴함
    record2 = cursor.fetchall()
    # 여러 개를 리턴하는 함수를 호출해서 데이터가 없다는 사실을 확인하는 방법은 데이터의 개수가 0인지 확인해야함
    if len(record2) == 0 :
        print("검색된 데이터가 없음")
    else :
        for attr2 in record2 :
            print(attr2)

    # 삽입할 이미지 파일의 내용 읽기
    # 자신의 파일 경로로 수정
    #f = open('newjeans.jpg', 'rb')
    #newjeans = f.read()
    #f.close()

    # 데이터 삽입
    #cursor.execute("INSERT INTO BLOBTABLE VALUES(%s, %s)",("newjeans.jpg", newjeans))
    #con.commit()

    # 데이터 읽어오기
    cursor.execute("SELECT * FROM BLOBTABLE")
    data = cursor.fetchone()
    # 두번째 데이터가 blob 이므로 두번째 데이터를 파일로 변경
    print(data[0])
    # 파일을 쓰기 모드로 생성
    f = open(data[0], 'wb')
    # 읽은 데이터를 파일에 기록
    f.write(data[1])
    f.close()

except :
    print("예외 발생:", sys.exc_info())
finally:
    if con != None:
        con.close()

=======
import sys
import pymysql
try :
    # 데이터베이스 연결 객체 생성
    con = pymysql.connect(host='localhost', port=3306, db='yeji', user='yeji', passwd='moon', charset='utf8')
    # SQL 실행 객체 생성
    cursor = con.cursor()
    # SQL 실행 - 값을 직접 SQL에 작성
    #cursor.execute("INSERT INTO DEPT VALUES(11,'비서','신안')")
    # SQL 실행 - SQL에 서식을 설정하고 파라미터를 대입하는 코드 작성
    # 12번 데이터의 부서를 영업 그리고 위치를 서초로 수정
    #cursor.execute("UPDATE DEPT SET DNAME = %s, LOC = %s WHERE DEPTNO = %s", ('영업','서초',12))
    # 12번 데이터 삭제
    #cursor.execute("DELETE FROM DEPT WHERE DEPTNO = %s", (12))

    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO > %s", (100))
    # 검색 된 결과가 없으면 None이고 존재하면 Tuple
    record = cursor.fetchone()
    if record == None :
        print("검색된 데이터가 없음")
    else :
        for attr in record :
            print(attr)
    # 검색 결과 전체 데이터를 읽어오는 것
    # 여러 개의 데이터를 가져오는 경우는 데이터가 없는 경우 빈 튜플을 리턴함
    record2 = cursor.fetchall()
    # 여러 개를 리턴하는 함수를 호출해서 데이터가 없다는 사실을 확인하는 방법은 데이터의 개수가 0인지 확인해야함
    if len(record2) == 0 :
        print("검색된 데이터가 없음")
    else :
        for attr2 in record2 :
            print(attr2)

    # 삽입할 이미지 파일의 내용 읽기
    # 자신의 파일 경로로 수정
    #f = open('newjeans.jpg', 'rb')
    #newjeans = f.read()
    #f.close()

    # 데이터 삽입
    #cursor.execute("INSERT INTO BLOBTABLE VALUES(%s, %s)",("newjeans.jpg", newjeans))
    #con.commit()

    # 데이터 읽어오기
    cursor.execute("SELECT * FROM BLOBTABLE")
    data = cursor.fetchone()
    # 두번째 데이터가 blob 이므로 두번째 데이터를 파일로 변경
    print(data[0])
    # 파일을 쓰기 모드로 생성
    f = open(data[0], 'wb')
    # 읽은 데이터를 파일에 기록
    f.write(data[1])
    f.close()

except :
    print("예외 발생:", sys.exc_info())
finally:
    if con != None:
        con.close()

>>>>>>> 75f497cf7d8abbee6808c9474159760ca148c6c0
