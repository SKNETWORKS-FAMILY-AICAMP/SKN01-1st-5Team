import pandas as pd
from crawlingDB.helpers.connectTB import ConnectTB
import pymysql
# info TB 만들기
   

def make_info(password='encore1234'):
    user = "encore"; host = "localhost"; port = 3306; db = "car"
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS info")
    query1 = '''
    CREATE TABLE info (  
    name varchar(255) ,
    address varchar(255),
    num varchar(255),
    PRIMARY KEY (name)
    ) 
    ''' 
    cur.execute(query1)

    query2 = "INSERT INTO info (name, address, num) VALUES (%s, %s, %s)"

    data = [
        ("genesis","서울시 강남구 영동대로 410","02-556-9870"),
        ("hyundai","서울특별시 서초구 양재동 231번지","080-600-6000"),
        ("kia","서울시 서초구 헌릉로 12","080-200-2000"),
        ("benz","서울시 중구 한강대로 416","02-6328-7700"),
        ("renault korea","부산광역시 강서구 신호산단3로 51","080-300-3000"),
        ("chevrolet","인천광역시 부평구 부평대로 233","080-3000-5000"),
        ("tesla","서울특별시 강남구 테헤란로 134","080-617-1390"),
        ("BMW","서울특별시 중구 퇴계로 100","080-269-2200"),
        ("audi","서울특별시 강남구 테헤란로 152","080-767-2834")
    ]

    cur.executemany(query2, data)

    conn.commit()

    cur.close()

# 디비에 csv 밀어넣기
def make_full_DB():
    user = "encore"; password = "encore1234"; host = "localhost"; port = 3306; db = "car"
    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
    cur = conn.cursor()

    genesis_df = pd.read_csv('C:\\Users\\SAMSUNG\\Desktop\\Workspace\\first_project\\result\\total_genesis.csv', encoding='utf-8')
    kia_df = pd.read_csv('C:\\Users\\SAMSUNG\\Desktop\\Workspace\\first_project\\result\\total_kia.csv', encoding='utf-8')
    hyundai_df = pd.read_csv('C:\\Users\\SAMSUNG\\Desktop\\Workspace\\first_project\\result\\total_hyundai.csv', encoding='utf-8')

    # genesis
    g = ConnectTB(db_url)
    cur.execute("DROP TABLE IF EXISTS genesis;")
    genesisTB = g.getTable('genesis')  # 테이블 이름을 동적으로 설정
    g.uploadTB() 
    session = g.getSession()
    for i in range(genesis_df.shape[0]):
        genesis_entry = genesisTB(brand='genesis', title=genesis_df['title'][i], context=genesis_df['context'][i]) 
        session.add(genesis_entry)
        
    session.commit()
    session.close()


    # kia
    k = ConnectTB(db_url)
    cur.execute("DROP TABLE IF EXISTS kia;")
    kiaTB = k.getTable('kia')
    k.uploadTB()
    session = k.getSession()
    for i in range(kia_df.shape[0]):
        kia_entry = kiaTB(brand='kia', title=kia_df['title'][i], context=kia_df['context'][i]) 
        session.add(kia_entry)
    session.commit()
    session.close()

    # hyundai
    h = ConnectTB(db_url)
    cur.execute("DROP TABLE IF EXISTS hyundai;")
    hyundaiTB = h.getTable('hyundai')
    h.uploadTB()
    session = h.getSession()
    for i in range(hyundai_df.shape[0]):
        hyundai_entry = hyundaiTB(brand='hyundai', title=hyundai_df['title'][i], context=hyundai_df['context'][i])
        session.add(hyundai_entry)
    session.commit()
    session.close()

    for tb in ['kia','hyundai','genesis']:
        SQL = f'ALTER TABLE {tb} ADD FOREIGN KEY (brand) REFERENCES info (name);'
        cur.execute(SQL)

    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    make_info()
    make_full_DB()
