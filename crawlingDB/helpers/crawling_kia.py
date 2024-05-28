import time
import os
import pandas as pd
from crawlingDB.helpers.base.crawling_sele import User

### KIA
def get_kia():
    browser=User()
    kia_url = r'https://www.kia.com/kr/customer-service/center/faq'

    browser.getBrowser(kia_url)

    browser.click_button("/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div/div/div/ul/li[2]/button")
    time.sleep(3)
    con_lst = []
    title_lst = []
    for k in range(5):
        try:
            for j in range(4):
                for i in range(10):
                    try:
                        title = f"/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{i+1}]/h3/button"
                        context = f"/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{i+1}]/div/div/div/div"
                        ti = browser.find_ele_text(title)
                        title_lst.append(ti)
                        browser.click_button(f"/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/div/div/div[{i+1}]/h3/button/span[1]")
                        time.sleep(2)
                        try: 
                            con = browser.find_ele_text(context)
                        except Exception:
                            con = None

                        con_lst.append(con)
                    except:
                        break
                
                browser.click_button(f"//*[@id='contents']/div/div[3]/div/div/div[4]/div/ul/li[{j+2}]/a")
                time.sleep(2)
            if k ==0:
                browser.click_button(f"/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div/button")
            else:
                browser.click_button(f"/html/body/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div/button[2]")
        except :
            break
            
    browser.close_connect() 
    if len(con_lst) == 0:
        print('검색 결과 0건입니다. 다른 단어로 찾아보세요!')
    else:
        df = pd.DataFrame({'title':title_lst, 'context':con_lst})
        df = df.dropna()
        df['context'] = df['context'].str.replace(r'\n', '', regex=True)
        print(f'Return 질문 {df['title'].count()}개 답변 {df['context'].count()}개.')

        result_path = os.path.join(os.getcwd(), 'result')
        os.makedirs(result_path, exist_ok=True)
        df.to_csv(os.path.join(result_path, 'total_kia.csv'), index=False, encoding='utf-8')
        print(f'{result_path}에 file이 저장되었습니다.')
        return df
