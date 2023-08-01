-- 데이터베이스 사용 설정
use yeji;
-- 데이터베이스에 존재하는 테이블 확인
show tables;

-- 현재 유저 확인
SELECT USER();

-- 현재 사용 중인 데이터베이스 확인
SELECT DATABASE();

-- MySQL은 매개변수가 없는 함수는 이름만으로 수행 가능

-- EMP 테이블에서 ENAME과 SAL, COMM을 조회
SELECT ENAME, SAL, COMM
FROM EMP;

-- EMP 테이블에서 ENAME과 SAL, COMM 그리고 SAL+COMM을 조회
-- NULL과 연산을 하면 결과는 NULL
SELECT ENAME, SAL, COMM, SAL+COMM AS 수령액
FROM EMP;

-- EMP 테이블에서 ENAME과 SAL, COMM 그리고 SAL+COMM을 조회
-- NULL과 연산을 하면 결과는 NULL
SELECT ENAME, SAL, COMM, SAL+IFNULL(COMM,0) AS 수령액
FROM EMP;

-- COMM이 NULL이 아니면 COMM을 COMM이 NULL이고 SAL이 NULL이 아니면 SAL을 리턴
SELECT COALESCE(COMM, SAL)
FROM EMP;

-- EMP 테이블의 데이터 개수를 조회
-- EMP 테이블에서 EMPNO가 NULL이 아닌 데이터의 개수를 조회
SELECT COUNT(EMPNO)
FROM EMP;

-- COMM이 NULL이 아닌 데이터 개수를 조회
SELECT COUNT(COMM)
FROM EMP;

-- 모든 컬럼이 NULL이 아닌 데이터 개수 조회
SELECT COUNT(*) AS cnt
FROM EMP;

-- EMP 테이블에서 SAL의 평균 구하기
SELECT AVG(SAL)
FROM EMP;

-- EMP 테이블에서 COMM의 평균 구하기
-- COMM은 4개의 데이터가 NULL이 아니고 10개의 데이터는 NULL
SELECT AVG(COMM)
FROM EMP;

SELECT SUM(COMM)/COUNT(*)
FROM EMP;

-- 위 2개의 결과는 다름
-- COMM이 NULL인 경우는 0으로 해서 평균을 계산
SELECT AVG(IFNULL(COMM,0))
FROM EMP;

-- EMP 테이블에서 ENAME과 데이터 개수를 조회 - 에러
SELECT ENAME, COUNT(*)
FROM EMP;

-- EMP 테이블에서 DEPTNO 별로 SAL의 평균 조회
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

-- EMP 테이블에서 DEPTNO 별로 DEPTNO, ENAME, SAL의 평균 조회 : 에러
-- GROUP BY가 있는 경우 GROUP BY 절에 없는 컬럼이나 연산식을 조회하면 행의 개수가 맞지 않아서 에러
SELECT DEPTNO, ENAME, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

-- tCity 테이블에서 region별 popu의 합계를 조회
SELECT region, sum(popu)
FROM tCity
GROUP BY region;

-- 2개 이상의 컬럼으로 그룹화가 가능
-- tStaff 테이블에서 depart, gender 별로 데이터 개수를 조회
SELECT depart, gender, count(*)
FROM tStaff
GROUP BY depart, gender
ORDER BY depart;

-- EMP 테이블에서 DEPTNO가 5번 이상 나오는 경우 DEPTNO와 SAL의 평균 조회
-- 이 경우는 그룹화되기 전에 그룹함수를 사용해서 에러
SELECT DEPTNO, AVG(SAL)
FROM EMP
WHERE COUNT(DEPTNO) >= 5
GROUP BY DEPTNO;

-- 그룹 함수를 이용한 조건은 HAVING절에 기재해야 함
SELECT DEPTNO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING COUNT(DEPTNO) >= 5;

-- tStaff 테이블에서 depart별로 salary가 340이 넘는 부서의 depart와 sal의 평균을 조회
SELECT DEPART, AVG(SALARY)
FROM tStaff
GROUP BY depart
HAVING AVG(SALARY) > 340;

-- tStaff 테이블에서 depart가 인사과나 영업부인 데이터의 depart와 salary의 최대값을 조회
-- 집계 함수를 사용하지 않아도 되므로 WHERE에 조건을 작성하는 것이 좋음
-- 방법1
SELECT DEPART, MAX(SALARY)
FROM tStaff
GROUP BY depart
HAVING DEPART IN ('인사과', '영업부'); -- IN 대신에 OR을 사용해도 됨
-- 방법2(추천)_필터링(WHERE)을 먼저 하는게 좋음
SELECT DEPART, MAX(SALARY)
FROM tStaff
WHERE DEPART IN ('인사과', '영업부')
GROUP BY depart ; 

-- EMP 테이블에서 SAL이 많은 순서부터 일련번호를 부여해서 ENAME과 SAL을 조회
SELECT ROW_NUMBER() OVER(ORDER BY SAL DESC) AS '급여가 많은 순서', ENAME, SAL
FROM EMP;
-- EMP 테이블에서 SAL이 많은 순서부터 동일한 값은 동일한 순위를 부여해서 ENAME과 SAL을 조회
SELECT DENSE_RANK() OVER(ORDER BY SAL DESC) AS '급여가 많은 순서', ENAME, SAL
FROM EMP;
-- 동일한 순위가 있으면 다음 순위는 건너뜀
SELECT RANK() OVER(ORDER BY SAL DESC) AS '급여가 많은 순서', ENAME, SAL
FROM EMP;
-- 그룹으로 분할 : 3등분
SELECT NTILE(3) OVER(ORDER BY SAL DESC) AS '급여가 많은 순서', ENAME, SAL
FROM EMP;
-- EMP 테이블에서 DEPTNO별로 SAL이 많은 순서부터 동일한 값은 동일한 순위를 부여해서 ENAME과 SAL을 조회
SELECT DEPTNO, DENSE_RANK() OVER(PARTITION BY DEPTNO ORDER BY SAL DESC) AS '급여가 많은 순서', ENAME, SAL
FROM EMP
ORDER BY DEPTNO;

-- EMP 테이블에서 SAL의 내림차순으로 정렬한 다음 데이터와의 SAL의 차이를 알고자 하는 경우
SELECT ENAME, SAL, SAL - (LEAD(SAL,1) OVER (ORDER BY SAL DESC)) AS "급여 차이"
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에서 SAL의 내림차순으로 정렬한 이전 데이터와의 SAL의 차이를 알고자 하는 경우
SELECT ENAME, SAL, SAL - (LAG(SAL,1) OVER (ORDER BY SAL DESC)) AS "급여 차이"
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에서 SAL의 내림차순으로 정렬한 첫번째 데이터와의 SAL의 차이를 알고자 하는 경우(최대값과의 차이)
SELECT ENAME, SAL, SAL - (FIRST_VALUE(SAL) OVER (ORDER BY SAL DESC)) AS "급여 차이"
FROM EMP
ORDER BY SAL DESC;
-- 급여의 누적 백분율
SELECT ENAME, SAL, CUME_DIST() OVER (ORDER BY SAL DESC)*100 AS "급여 차이"
FROM EMP
ORDER BY SAL DESC;

-- EMP 테이블에는 JOB과 DEPTNO와 SAL항목이 존재
-- JOB별 그리고 DEPTNO별 SAL의 합계를 구하고자 함

SELECT JOB, DEPTNO, SUM(SAL)
FROM EMP
GROUP BY JOB, DEPTNO;

-- PIVOT 이용
SELECT JOB,
	SUM(IF(DEPTNO=10, SAL, 0)) AS '10',
	SUM(IF(DEPTNO=20, SAL, 0)) AS '20',	
	SUM(IF(DEPTNO=30, SAL, 0)) AS '30',
	SUM(SAL) AS '합계'
FROM EMP
GROUP BY JOB;

-- JSON 출력
SELECT JSON_OBJECT("ename", ENAME, "sal", SAL) AS 'JSON 조회'
FROM EMP;


-- EMP 테이블에서 DEPTNO를 조회 : 10, 20, 30
SELECT DISTINCT DEPTNO
FROM EMP;

-- DEPT 테이블에서 DEPTNO를 조회 : 10, 20, 30, 40
SELECT DEPTNO
FROM DEPT;

-- EMP 테이블과 DEPT 테이블의 DEPTNO의 합집합 : 10, 20, 30, 40 (중복이 제거됨)
SELECT DISTINCT DEPTNO
FROM EMP
UNION
SELECT DEPTNO
FROM DEPT;

SELECT DISTINCT DEPTNO
FROM EMP
UNION ALL
SELECT DEPTNO
FROM DEPT;

-- EMP 테이블과 DEPT 테이블의 DEPTNO의 교집합 : 10, 20, 30
SELECT DEPTNO
FROM EMP
INTERSECT
SELECT DEPTNO
FROM DEPT;

-- DEPT 테이블에는 존재하지만 EMP 테이블에는 존재하지 않는 DEPTNO : 40
SELECT DEPTNO
FROM DEPT
EXCEPT
SELECT DEPTNO
FROM EMP;

-- 테이블 구조 확인
DESC EMP;
DESC DEPT;

-- ENAME이 MILLER인 사원의 DNAME을 조회
SELECT DEPTNO
FROM EMP
WHERE ENAME='MILLER';

SELECT DNAME
FROM DEPT
WHERE DEPTNO = 10;

-- SUB QUERY를 이용한 해결
-- 괄호 안의 Sub Query를 먼저 수행해서 10을 찾아오고 그 값을 이용해서 DNAME을 조회
SELECT DNAME
FROM DEPT
WHERE DEPTNO = (SELECT DEPTNO
				FROM EMP
				WHERE ENAME='MILLER');

-- EMP 테이블에서 SAL의 평균보다 더 많은 SAL을 받는 직원의 ENAME과 SAL을 조회
SELECT ENAME, SAL
FROM EMP
WHERE SAL >= (SELECT AVG(SAL) FROM EMP)
ORDER BY SAL DESC;

-- EMP 테이블에서 ENAME이 MILLER인 사원과 동일한 직무(JOB)를 가진 사원의 ENAME과 JOB을 조회
-- MILLER는 제외
SELECT ENAME, JOB
FROM EMP
WHERE JOB = (SELECT JOB FROM EMP WHERE ENAME='MILLER') AND ENAME!='MILLER';

-- EMP 테이블에서 DEPT 테이블의 LOC가 DALLAS인 사원의 ENAME과 SAL을 조회
SELECT ENAME, SAL
FROM EMP
WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE LOC='DALLAS');

-- EMP 테이블에서 DEPTNO 별 SAL의 최대값과 동일한 SAL을 갖는 사원의 EMPNO, ENAME, SAL을 조회
-- 이 구문은 에러 : 서브 쿼리의 결과가 3개라서 = 로 비교가 불가능
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE SAL = (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);

-- 서브 쿼리의 결과가 2개 이상인 경우는 그 중의 하나의 값과 일치하면 됨
SELECT EMPNO, ENAME, SAL
FROM EMP
WHERE SAL IN (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);

-- EMP 테이블에서 DEPTNO가 30인 데이터의 SAL보다 큰 데이터의 ENAME과 SAL을 조회 > 오류발생
-- DEPTNO가 30인 데이터는 2개 이상이므로 > 로는 비교가 불가능
SELECT ENAME, SAL
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE DEPTNO = 30);

-- 모든 데이터보다 커야 하는 경우는 ALL을 같이 사용
-- 방법1
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ALL(SELECT SAL FROM EMP WHERE DEPTNO = 30);
-- 방법2
SELECT ENAME, SAL
FROM EMP
WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = 30);

-- 데이터 중 1개보다만 크면 되는 경우는 ANY를 같이 사용
-- 방법1
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ANY(SELECT SAL FROM EMP WHERE DEPTNO = 30);
-- 방법2
SELECT ENAME, SAL
FROM EMP
WHERE SAL > (SELECT MIN(SAL) FROM EMP WHERE DEPTNO = 30);

-- EMP 테이블에서 SAL이 2000이 넘는 데이터가 있으면 ENAME과 SAL을 조회
-- 2000이 넘는 데이터가 존재하므로 모든 데이터를 조회
SELECT ENAME, SAL
FROM EMP
WHERE EXISTS(SELECT 1 FROM EMP WHERE SAL > 2000);

-- Cartesian Product(교차 곱)
-- FROM 절에 테이블 이름이 2개 이상이고 JOIN 조건이 없는 경우
-- EMP 테이블은 8열 14행, DEPT 테이블은 3열 4행
-- 결과는 11열 16행
SELECT *
FROM EMP, DEPT;

-- EQUI JOIN(동등 조인)
-- FROM 절에 테이블 이름이 2개 이상이고 WHERE 절에 2개 테이블의 공통된 컬럼의 값이 같다라는 조인 조건이 있는 경우
SELECT *
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO ;
-- 한쪽 테이블에만 존재하는 컬럼을 출력할 때는 컬럼 이름만 기재해도 됨
SELECT ENAME, DNAME, LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO ;
-- 양 쪽 테이블에 모두 존재하는 컬럼의 경우는 앞에 테이블 이름을 명시해야만 함
-- 테이블 이름을 명시하지 않으면 이름이 애매 모호하다고 에러가 발생
SELECT ENAME, DNAME, DEPTNO, LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO ;

-- 어떤 테이블의 DEPTNO인지 명시해주면 됨
SELECT ENAME, DNAME, EMP.DEPTNO, LOC
FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO ;

-- 테이블 이름에 새로운 이름 부여
SELECT ENAME, e.DEPTNO, DNAME, LOC
FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;

-- FROM에서 부여하는 것은 새로운 이름을 부여하는 것으로 기존 이름은 이제 사용할 수 없음
SELECT ENAME, e.DEPTNO, DNAME, LOC
FROM EMP e, DEPT d
WHERE e.DEPTNO = DEPT.DEPTNO;

-- HASH JOIN
SELECT /*+ ORDERED USE_HASH(E) */
ENAME, e.DEPTNO, DNAME, LOC
FROM DEPT d, EMP e -- DEPT 테이블이 행의 개수가 4개로 더 적어서 앞에다가 적어줘야 함
WHERE d.DEPTNO=e.DEPTNO;

-- NON EQUI JOIN
-- EMP 테이블의 SAL은 급여입니다.
-- SALGRADE 테이블의 LOSAL은 최저급여, HISAL은 최대급여, GRADE는 등급
-- EMP 테이블에서 ENAME과 SAL을 조회하고 SAL에 해당하는 GRADE를 조회하고자 하는 경우
SELECT ENAME, SAL, GRADE
FROM EMP, SALGRADE
WHERE SAL BETWEEN LOSAL AND HISAL;

-- EMP 테이블에서 ENAME과 관리자ENAME을 조회
-- 앞의 EMP는 현재 종업원이 되고 뒤의 EMP는 관리자
-- 종업원의 관리자 사원번호와 일치하는 관리자의 사원번호를 찾아서 이름을 조회
SELECT employee.ename, manager.ename
FROM EMP AS employee, EMP AS manager
WHERE employee.mgr = manager.empno;

-- ANSI CROSS JOIN
SELECT *
FROM EMP CROSS JOIN DEPT;

-- EMP 테이블과 DEPT 테이블의 INNER JOIN
SELECT *
FROM EMP INNER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;
-- 2개의 컬럼 이름이 같은 경우 USING 사용 가능
SELECT *
FROM EMP INNER JOIN DEPT
USING(DEPTNO);
-- 2개의 컬럼 이름이 같은 경우 NATURAL JOIN 사용 가능
-- 동일한 컬럼을 1번만 출력
SELECT *
FROM EMP NATURAL JOIN DEPT;

-- OUTER JOIN
SELECT DISTINCT DEPTNO
FROM EMP;

SELECT DEPTNO
FROM DEPT;

-- EMP에 존재하는 모든 DEPTNO가 JOIN에 참여
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO ;
-- DEPT에 존재하는 모든 DEPTNO가 JOIN에 참여
-- DEPT에는 존재하지만 EMP에는 존재하지 않는 40이 JOIN에 참여
-- 이 경우 40은 자신의 데이터 말고는 NULL
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO ;

-- MySQL은 FULL OUTER JOIN을 지원하지 않음
SELECT *
FROM EMP FULL OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO ;

-- FULL OUTER JOIN을 UNION으로 해결
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO 
UNION
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO ;