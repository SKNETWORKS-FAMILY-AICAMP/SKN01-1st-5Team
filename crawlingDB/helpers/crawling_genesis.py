import time
import os
import pandas as pd
from crawlingDB.helpers.base.crawling_sele import User

### GENESIS
def get_genesis():
    browser=User()
    genesis_url = 'https://www.genesis.com/kr/ko/support/faq.html'
    # 현대 FAQ 접근
    browser.getBrowser(genesis_url)
    browser.scroll_down(10000, init_pos=True)
    time.sleep(3)
    browser.scroll_down(500, init_pos=True)

    con_lst = []
    title_lst = []
    for i in range(193):
        try:
            title = f'/html/body/div[2]/div[2]/div[4]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[{i+1}]/a/p'
            context =f'/html/body/div[2]/div[2]/div[4]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[{i+1}]/div/div'

            ti = browser.find_ele_text(title)
            browser.click_button(title)
            time.sleep(2)
            con = browser.find_ele_text(context)
            time.sleep(2)
            browser.click_button(title)
            time.sleep(1)
            con_lst.append(con)
            title_lst.append(ti)
        except Exception as e:
            break
    browser.close_connect() 
    if len(con_lst) == 0:
        print('크롤링되지 않음')
    else:
        df = pd.DataFrame({'title':title_lst, 'context':con_lst})
        df['context'] = df['context'].str.replace(r'\n', '', regex=True)
        print(f'Return 질문 {len(title_lst)}개 답변 {len(con_lst)}개.')

      
        result_path = os.path.join(os.getcwd(), 'result')
        os.makedirs(result_path, exist_ok=True)
        df.to_csv(os.path.join(result_path, 'total_genesis.csv'), index=False, encoding='utf-8')
        print(f'{result_path}에 file이 저장되었습니다.')