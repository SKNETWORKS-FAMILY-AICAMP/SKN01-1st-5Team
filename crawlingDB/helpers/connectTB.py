from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
# from helpers.make_brandTB import Base, name_of_brand_TB
from crawlingDB.helpers.make_brandTB import Base, name_of_brand_TB

class ConnectTB:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def uploadTB(self):
        Base.metadata.create_all(self.engine)

    def getSession(self):
        return self.Session()

    def getTable(self, table_name):
        return name_of_brand_TB(table_name)

