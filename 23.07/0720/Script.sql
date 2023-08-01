use yeji;

-- SELECT 구문 실행 : 트랜잭션과 아무런 연관성이 없음
SELECT * FROM DEPT;

-- DEPT 테이블에 데이터를 1개 삽입 : 이전 트랜잭션이 없어서 트랜잭션이 생성
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(50, '회계', '서울');

SELECT * FROM DEPT;

-- 철회 : SAVEPOINT를 입력하지 않으면 트랜잭션 시작 전으로 복구
ROLLBACK;

SELECT * FROM DEPT;
-- 삽입 - 트랜잭션이 생성
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(50, '회계', '서울');
-- DEPT 테이블의 모든 내용을 가진 DEPTCOPY 테이블을 생성
-- DDL(CREATE, DROP, ALTER, TRUNCATE, RENAME), DCL(GRANT, REVOKE)를 수행하면 AUTO COMMIT
-- COMMIT 수행 : 트랜잭션은 변경 내용을 반영하고 종료
CREATE TABLE DEPTCOPY
AS
SELECT * FROM DEPT;

-- 철회 : INSERT > CREATE > ROLLBACK 순으로 하면 CREATE를 하는 순간 AUTO COMMIT이 되어서 INSERT가 롤백이 안됨!
ROLLBACK;
SELECT * FROM DEPT;

SHOW TABLES;
-- 트랜잭션 생성
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(60, '회계', '서울');
SAVEPOINT SV1;
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(70, '회계', '서울');
SAVEPOINT SV2;
INSERT INTO DEPT(DEPTNO, DNAME, LOC) VALUES(80, '회계', '서울');

SELECT * FROM DEPT;
-- SV1을 생성한 지점으로 이동
ROLLBACK TO SV1;
SELECT * FROM DEPT;

-- COMMIT;



-- 일반적인 JOIN 방법을 이용해서 JOB이 CLERK인 데이터의 정보를 조회
-- 방법1
SELECT *
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO AND JOB = 'CLERK';
-- 방법2 : 미리 걸러서 갯수를 줄이는 방법 / TEMP라는 임시 테이블을 만들어서(JOB이 CLERK인 테이블) 좀 더 효율적
SELECT *
FROM (SELECT * FROM EMP WHERE JOB = 'CLERK') TEMP, DEPT
WHERE TEMP.DEPTNO = DEPT.DEPTNO;


-- EMP 테이블에서 EMPNO, ENAME, SAL, COMM 만으로 구성된 뷰를 생성
CREATE VIEW KIM
AS
SELECT EMPNO, ENAME, SAL, COMM
FROM EMP;

-- VIEW는 테이블 처럼 사용
SELECT *
FROM KIM;

-- VIEW에 DML(삽입, 삭제, 갱신) 작업은 가능한 경우도 있고 가능하지 않은 경우도 있음
DESC EMP;

-- VIEW에 데이터 삽입 : 뷰를 만들 때 사용한 EMP 테이블에 데이터가 삽입됨(뷰랑 원본테이블 둘 다 추가됨)
INSERT INTO KIM(EMPNO, ENAME, SAL, COMM) VALUES(9999,'ADAM',10000,9000);
SELECT *
FROM KIM;

SELECT *
FROM EMP;

-- 뷰의 구조 확인
DESC KIM;

-- 뷰 삭제
DROP VIEW KIM;

-- 임시 테이블 생성 : 접속을 해제한 후 다시 연결하면 이 테이블은 소멸됨
CREATE TEMPORARY TABLE TEMP(
	NAME CHAR(20)
);
SELECT * FROM TEMP;

-- CTE : SQL 수행 중에만 일시적으로 메모리 공간을 할당받아서 사용하는 테이블
-- SELECT 구문의 결과를 일시적으로 TEMP라는 테이블 이름을 부여해서 보관
-- CTE를 생성하는 구문은 가장 먼저 수행됨
-- 이와 유사한 작업을 INLINE VIEW를 할 수 있을 것 처럼 보이지만 INLINE VIEW는 Sub Query 보다 늦게 수행되기 때문에
-- INLINE VIEW는 Sub Query에 사용할 수 없음
SELECT *
FROM (SELECT NAME, SALARY, SCORE FROM tStaff WHERE DEPART = '영업부' AND GENDER = '남') TEMP
WHERE SALARY >= (SELECT AVG(SALARY) FROM (SELECT NAME, SALARY, SCORE FROM tStaff WHERE DEPART = '영업부' AND GENDER = '남') TEMP);
-- WITH를 사용하는 방법(최종)
WITH TEMP AS
(SELECT NAME, SALARY, SCORE FROM tStaff WHERE DEPART = '영업부' AND GENDER = '남')
SELECT * FROM TEMP WHERE SALARY >= (SELECT AVG(SALARY) FROM TEMP);

-- usertbl 테이블 존재 여부 확인
SHOW TABLES;
DESC usertbl;
SELECT *
FROM usertbl;

DROP PROCEDURE myproc;
-- DELIMITER는 프로시저 종료를 알리기 위한 기호를 설정하는 것인데 2개로 만드는 이유는
-- 하나 짜리로 만들면 데이터로 사용되는 것과 혼동이 올 수 있어서
-- DBeaver에서 수행할 때는 SQL 스크립트 실행으로 실행해야함
-- 파이썬의 함수와 비슷함
DELIMITER //
CREATE PROCEDURE myproc(vuserid char(15), vname varchar(20), vbirthday int(11), vaddr char(100), vmobile char(11), vmdate date)
		BEGIN
			INSERT INTO usertbl
			VALUES(vuserid, vname, vbirthday, vaddr, vmobile, vmdate);
		END //
DELIMITER ;

CALL myproc('MANSIK','정만식',1974,'목포','01011112222','1974-12-11');
CALL myproc('MANSIK2','정만식',1974,'목포','01011112222','1974-12-11');

SELECT *
FROM usertbl;

-- 트리거를 수행하기 위한 샘플 테이블 생성
CREATE TABLE EMP01(
	EMPNO INT PRIMARY KEY,
	ENAME VARCHAR(30) NOT NULL,
	JOB VARCHAR(100)
);

CREATE TABLE SAL01(
	SALNO INT PRIMARY KEY AUTO_INCREMENT,
	SAL FLOAT(7,2),
	EMPNO INT REFERENCES EMP01(EMPNO) ON DELETE CASCADE
);

SHOW TABLES;
-- EMP01 테이블에 데이터를 추가하면 SAL01테이블에 데이터가 자동으로 추가되는 트리거
DELIMITER //
CREATE TRIGGER trg_01
AFTER INSERT ON EMP01
FOR EACH ROW
BEGIN
	INSERT INTO SAL01(SAL,EMPNO) VALUES(100, NEW.EMPNO);
END //
DELIMITER ;

INSERT INTO EMP01 VALUES(1,'아담','프로그래머');

SELECT *
FROM EMP01;

SELECT *
FROM SAL01;

