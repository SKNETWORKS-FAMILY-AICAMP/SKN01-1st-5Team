from sqlalchemy import Integer, String, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base

# 테이블 생성을 위함
Base = declarative_base()

class BrandTB:
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(10),)
    title = Column(String(1000))
    context = Column(String(6000))

def name_of_brand_TB(table_name):
    # 동적으로 테이블 이름을 설정하는 클래스 생성
    return type(table_name, (Base, BrandTB), {'__tablename__': table_name, '__table_args__': {'extend_existing': True}})