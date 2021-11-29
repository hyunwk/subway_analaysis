# 라이브러리 설치 (주피터 노트북)
import pandas
import sqlalchemy
import pymysql

# 라이브러리 임포트
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# pymysql 세팅
db = pymysql.connect(user='root', host='localhost', passwd='',port=3306, db='subway')
cursor = db.cursor()

# csv파일 불러오기
df = pd.read_csv('파일명.csv',encoding = 'utf-8-sig')
df.columns = ['테이블과 동일한 컬럼명 사용하도록 수정']

# sqlalchemy를 사용해 원하는 database에 csv파일 저장
engine = create_engine("mysql+pymysql://유저이름:"+"비밀번호"+"@호스트주소:포트숫자/데이터베이스이름?charset=utf8", encoding = "utf-8")
conn = engine.connect()
df.to_sql(name = "테이블이름", con = engine, if_exist = 'append', index = False)
conn.close()

# 저장 확인
sql = "select * from 테이블이름 limit 5"
pd.read_sql(sql,db)