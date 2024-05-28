from crawlingDB.helpers.connectTB import ConnectTB

def get_by_sql(table_name, keyword, password='encore1234'):
    user = "encore"; host = "localhost"; port = 3306; db = "car"
    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"

    conn = ConnectTB(db_url)
    session = conn.getSession()
    tb = conn.getTable(table_name)
    q = session.query(tb).filter(tb.context.like(f'%{keyword}%')).all()

    if not q:
        print('검색결과가 존재하지 않습니다. 다른 단어로 검색해주세요!')
    title_lst = []
    context_lst = []
    for result in q:
        title_lst.append(result.title)
        context_lst.append(result.context)
    return title_lst, context_lst



if __name__ == '__main__':
    results = get_by_sql('비용')
    for result in results:
        print(result.title)
        print(result.context)
