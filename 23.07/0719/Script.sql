-- 데이터베이스 사용 설정
use yeji;

-- 테이블 생성
-- 테이블 이름은 contact
-- 속성
	-- num은 정수이고 일련번호 그리고 기본키
	-- name은 한글 7자까지 저장하고 글자 수는 변경되지 않는다고 가정
	-- address는 한글 100자까지 저장하고 글자 수의 변경이 자주 발생
	-- tel은 숫자로된 문자열 11자리이고 글자수의 변경은 발생하지 않음
	-- email은 영문 100자 이내이고 글자 수의 변경이 자주 발생
	-- birthday는 날짜만 저장
	-- 주로 조회를 하고 일련번호는 1부터 시작하고 인코딩은 utf8

CREATE TABLE contact(
	num INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(21),
	address TEXT,
	tel VARCHAR(11),
	email CHAR(100),
	birthday DATE
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- contact 테이블에 age 컬럼을 정수 자료형으로 추가
ALTER TABLE contact
ADD age INTEGER;

-- contact 테이블 구조 확인
DESC contact;

-- contact 테이블에서 age 컬럼 삭제
ALTER TABLE contact
DROP age;

DESC contact;

-- contact 테이블에서 tel 컬럼의 이름을 phone으로 자료형은 정수로 수정
ALTER TABLE contact 
CHANGE tel phone INTEGER;

DESC contact;

-- contact 테이블 삭제
DROP TABLE contact;

SHOW TABLES;

-- DEPT 테이블은 EMP 테이블에서 DEPTNO 컬럼을 참조하므로 삭제가 안됨
DROP TABLE DEPT;

-- NOT NULL 제약조건 설정
CREATE TABLE tNullable(
	name CHAR(10) NOT NULL,
	age INT
);

INSERT INTO tNullable(name, age) VALUES("adam", 23);
-- 에러
INSERT INTO tNullable(age) VALUES(23); 

-- 연습한거 지우기
DROP TABLE tNullable;


-- 기본값 설정
CREATE TABLE tDefault(
	name CHAR(10) NOT NULL,
	age INTEGER DEFAULT 0
);

INSERT INTO tDefault(name, age) VALUES('adam', 53);
-- 기본값이 설정된 컬럼을 제외하고 입력하면 그 컬럼에는 기본값이 삽임됨
INSERT INTO tDefault(name) VALUES('jessica');

-- 데이터 확인
SELECT *
FROM tDefault;


-- name, gender(성별-남 또는 여), age(나이는 양수)를 속성으로 갖는 테이블을 생성
create table tcheck(
	name CHAR(10) NOT NULL,
	gender CHAR(3) CHECK(gender IN('남','여')),
	age INT CHECK(age >= 0)
);

INSERT INTO tcheck(name,gender,age) VALUES('김좌진', '남', 53);
-- age가 음수라서 에러
INSERT INTO tcheck(name,gender,age) VALUES('홍범도', '남', -23);
-- gender가 여자라서 에러
INSERT INTO tcheck(name,gender,age) VALUES('유관순', '여자', 32);

SELECT *
FROM tcheck;



-- 기본키 설정 : 제약조건 이름없이 생성
CREATE TABLE tPK1(
	name CHAR(10) PRIMARY KEY,
	age INT
);

-- 기본키 설정 : 제약조건 이름없이 생성
CREATE TABLE tPK2(
	name CHAR(10),
	age INT,
	CONSTRAINT tPK2_PK PRIMARY KEY(name)
);

-- 2개의 컬럼으로 기본키 설정 : 테이블을 생성할 때 PRIMARY KEY는 한번만 사용 가능
CREATE TABLE tPK3(
	name CHAR(10) PRIMARY KEY,
	age INT PRIMARY KEY,
);--틀린방법

CREATE TABLE tPK3(
	name CHAR(10),
	age INT,
	CONSTRAINT PK_tPK3 PRIMARY KEY(name,age)
);

INSERT INTO tPK1(name, age) VALUES('adam', 53);
-- 기본키인 name의 값이 같아서 삽입 실패
INSERT INTO tPK1(name, age) VALUES('adam', 54);
-- 기본키인 name의 값이 NULL 삽입실패
INSERT INTO tPK1(age) VALUES(54);

-- 
CREATE TABLE tUnique(
	name CHAR(10),
	age INT UNIQUE,
	CONSTRAINT tUnique PRIMARY KEY(name)
);
INSERT INTO tUnique(name, age) VALUES('adam', 54);
-- age가 중복되서 삽입 실패
INSERT INTO tUnique(name, age) VALUES('jessica', 54);
-- unique는 NULL은 삽입 가능
INSERT INTO tUnique(name) VALUES('jessica');
INSERT INTO tUnique(name) VALUES('hunter');

SELECT *
FROM tUnique;


-- 외래키를 지정하지 않는 2개의 테이블

-- 직원 테이블
CREATE TABLE tEmployee(
	name CHAR(10) PRIMARY KEY,
	salary INT NOT NULL,
	addr VARCHAR(30) NOT NULL);

INSERT INTO tEmployee VALUES('아이린', 650, '대구');
INSERT INTO tEmployee VALUES('정만식', 673, '목포');
INSERT INTO tEmployee VALUES('이국종', 1000, '양천구');

SELECT *
FROM tEmployee;

-- 프로젝트 테이블
-- employee는 프로젝트에 참여한 직원 이름
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10) NOT NULL,
	project VARCHAR(30) NOT NULL,
	cost INT
);

INSERT INTO tProject VALUES(1,'아이린','웹 서비스',3000);
-- 조이는 tEmployee 테이블에 없는 이름인데도 삽입이 가능
INSERT INTO tProject VALUES(2,'조이','MicroService 구축',10000);

SELECT *
FROM tProject;

-- 기존 테이블 삭제
DROP TABLE tEmployee;
DROP TABLE tProject;

-- 테이블 존재 여부 확인
SHOW TABLES;



-- 프로젝트 테이블
-- employee는 프로젝트에 참여한 직원 이름
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10) NOT NULL,
	project VARCHAR(30) NOT NULL,
	cost INT,
	CONSTRAINT FK_emp FOREIGN KEY(employee) REFERENCES tEmployee(name)
);

INSERT INTO tProject VALUES(1,'아이린','웹 서비스',3000);
-- 조이는 tEmployee 테이블에 없는 이름이라서 삽입 불가
INSERT INTO tProject VALUES(2,'조이','MicroService 구축',10000);
-- tEmployee 테이블의 데이터를 삭제
DELETE FROM tEmployee WHERE name = '정만식';
-- 아이린은 tProject 테이블에서 참조하고 있기 때문에 삭제가 불가능
DELETE FROM tEmployee WHERE name = '아이린';
-- tEmployee 테이블 삭제 불가능
DROP TABLE tEmployee;

-- 실습을 위해서 기존 테이블 삭제
DROP TABLE tProject;
DROP TABLE tEmployee;
SHOW TABLES;

-- 삭제 후 다시 만들었음
CREATE TABLE tEmployee(
	name CHAR(10) PRIMARY KEY,
	salary INT NOT NULL,
	addr VARCHAR(30) NOT NULL);

INSERT INTO tEmployee VALUES('아이린', 650, '대구');
INSERT INTO tEmployee VALUES('정만식', 673, '목포');
INSERT INTO tEmployee VALUES('이국종', 1000, '양천구');

SELECT *
FROM tEmployee;
-- tEmployee 테이블에 name이 수정되거나 삭제될 때 같이 수정되거나 삭제됨
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10) NOT NULL,
	project VARCHAR(30) NOT NULL,
	cost INT,
	CONSTRAINT FK_emp FOREIGN KEY(employee) REFERENCES tEmployee(name)
		ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO tProject VALUES(1,'아이린','웹 서비스',3000);

SELECT *
FROM tProject;

-- tEmployee 테이블에서 아이린을 배주현으로 수정
UPDATE tEmployee SET name= '배주현' WHERE name='아이린';

SELECT *
FROM tEmployee;

SELECT *
FROM tProject;

-- tEmployee 테이블에서 배주현을 삭제 : tProject에서도 연쇄 삭제가 발생
DELETE FROM tEmployee WHERE name='배주현';

SELECT *
FROM tEmployee;

SELECT *
FROM tProject;



-- set null 사용해보기
DROP TABLE tProject;

-- tEmployee 테이블에 name이 수정되거나 삭제될 때 null로 수정됨
CREATE TABLE tProject(
	projectid INT PRIMARY KEY,
	employee CHAR(10),
	project VARCHAR(30) NOT NULL,
	cost INT,
	CONSTRAINT FK_emp FOREIGN KEY(employee) REFERENCES tEmployee(name)
		ON DELETE SET NULL ON UPDATE SET NULL
);
INSERT INTO tEmployee VALUES('아이린', 650, '대구');
INSERT INTO tProject VALUES(1,'아이린','웹 서비스',3000);

SELECT *
FROM tProject;

-- tEmployee 테이블에서 아이린을 배주현으로 수정 : employee값이 null로 설정
UPDATE tEmployee SET name= '배주현' WHERE name='아이린';

SELECT *
FROM tEmployee;

SELECT *
FROM tProject;

-- 일련번호 사용
CREATE TABLE BOARD(
	num INT AUTO_INCREMENT PRIMARY KEY,-- PRIMARY KEY 혹은 UNIQUE 지정 필수
	title CHAR(100),
	content TEXT
);
	
INSERT INTO BOARD(title, content) VALUES("제목1","내용1");
INSERT INTO BOARD(title, content) VALUES("제목2","내용2");
-- 자동으로 1,2 순서대로 삽입
SELECT * FROM BOARD;

-- 2번 데이터 삭제
DELETE FROM BOARD WHERE num=2;
SELECT * FROM BOARD;
INSERT INTO BOARD(title, content) VALUES("제목3","내용3");
SELECT * FROM BOARD; -- 2번 지우고 다시 넣어도 일련번호는 2번으로 부여되지 않고 3번으로 부여됨

-- AUTO_INCREMENT 값도 직접 삽입이 가능
INSERT INTO BOARD(num, title, content) VALUES(200, "제목3","내용3");
SELECT * FROM BOARD; -- num=200으로 부여
INSERT INTO BOARD(title, content) VALUES("제목4","내용4");
SELECT * FROM BOARD; -- 그 후에 값을 추가하면 일련번호는 201로 부여됨

-- 일련번호 초기화
ALTER TABLE BOARD AUTO_INCREMENT = 1000;
INSERT INTO BOARD(title, content) VALUES("제목5","내용5");-- 1000으로 초기화 후 추가하면 일련번호는 1000으로 부여됨
SELECT * FROM BOARD;
-- 제약 조건 조회
SELECT *
FROM information_schema.table_constraints;

-- 데이터 삽입을 위해서 테이블 구조를 확인
DESC tCity;

-- 컬럼 이름을 나열해서 데이터 삽입
INSERT INTO tCity(name, area, popu, metro, region)
VALUES('평택', 200, 130, 'n', '경기');

-- 모든 컬럼에 값을 순서대로 입력하는 경우는 컬럼 이름 생략이 가능
INSERT INTO tCity
VALUES('목포', 23, 53, 'n', '전라');

-- NOT NULL이 설정된 컬럼을 제외하고는 생략하고 삽입 가능
INSERT INTO tCity(name, area, metro, region)
VALUES('여수', 25, 'n', '전라');

SELECT *
FROM tCity;

-- 한꺼번에 삽입
INSERT INTO tCity(name, area, metro, region)
VALUES('대전', 120, 'y', '충청'),('마산', 87, 'n', '경상');


SELECT *
FROM tCity;

-- tCity 테이블에서 name이 대전인 데이터 삭제
DELETE FROM tCity WHERE name = '대전';

-- tCity 테이블에서 name이 마산인 데이터의 popu를 40으로 수정
UPDATE tCity SET popu = 40 WHERE name = '마산';
