import time
import os
import pandas as pd
import selenium.common
import selenium
from crawlingDB.helpers.base.crawling_sele import User
User

### HYUNDAI
def get_hyundai(keyword=None):
    browser= User()
    hyundai_url = 'https://www.hyundai.com/kr/ko/e/customer/center/faq'
    # 현대 FAQ 접근
    browser.getBrowser(hyundai_url)

    # 차량구매 ~ 기타까지 페이지 수
    page_list = [4, 4, 4, 2, 8, 3, 2, 1, 1]
    last_qustions = [6, 10, 2, 1, 6, 9, 7, 7, 1]

    
    time.sleep(2)

    con_lst = []
    title_lst = []
    for i in range(9):
        try:
            browser.scroll_down(600)
            for j in range(1, page_list[i] + 1):
                browser.scroll_down(600, True)

                if j == page_list[i]:
                    for k in range(1, last_qustions[i] + 1):
                        time.sleep(1)
                        try:
                            x = browser.find_ele(f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{k}]/button/div/span[2]')
                            x.click()
                        except selenium.common.exceptions.NoSuchElementException:
                            print(i, j, k)
                            break
                        
                        y = browser.find_ele_text(f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{k}]/div/div')
                        print(x.text)
                        title_lst.append(x.text.strip())
                        con_lst.append(y)
                        time.sleep(2)

                else:
                    for k in range(1, 11):
                        time.sleep(1)
                        try:
                            x = browser.find_ele(f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{k}]/button/div/span[2]')
                            x.click()
                        except selenium.common.exceptions.NoSuchElementException:
                            print(i, j, k)
                            break

                        y = browser.find_ele_text(f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[1]/div[{k}]/div/div')
                        print(x.text)
                        title_lst.append(x)
                        con_lst.append(y)
                        time.sleep(2)

                if j < page_list[i]: 
                    button = browser.find_ele(f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/div/ul/li[{j + 1}]/button')
                    button.click()
                    time.sleep(2)

            if i != 8:
                browser.scroll_down(200)
                time.sleep(1)
                nxt = browser.find_ele(f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[{i + 2}]/button')
                nxt.click()
                time.sleep(1)
                button = browser.find_ele('//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[3]/div[2]/div/ul/li[1]/button')
                button.click()
                time.sleep(2)

            else:
                break
        except:
            break

        print(f'{i+1}번 페이지 완료')

    print(*title_lst, sep="\n")
    print(*con_lst, sep="\n")

    df = pd.DataFrame({'title':title_lst, 'context':con_lst})

    df['context'] = df['context'].str.replace(r'\n', '', regex=True)
    print(f'Return 질문 {len(title_lst)}개 답변 {len(con_lst)}개.')
    # save
    result_path = os.path.join(os.getcwd(), 'result')
    os.makedirs(result_path, exist_ok=True)
    df.to_csv(os.path.join(result_path, 'total_hyundai.csv'), index=False, encoding='utf-8')
    print(f'{result_path}에 file이 저장되었습니다.')

    return df
    