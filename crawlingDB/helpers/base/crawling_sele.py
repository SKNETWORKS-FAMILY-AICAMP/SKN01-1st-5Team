import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\\Users\\SAMSUNG\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

class User:
    def __init__(self):
        self.new_window = True
        self.options = Options()
        self.options.add_experimental_option("detach", True) 
        self.browser  = webdriver.Chrome(options=self.options)
        self.browser.maximize_window()
        self.scroll_pos = 0 

    def getBrowser(self, url='https://naver.com', new_window=True, option=None):  
        if new_window == False:
            print('디버깅 모드를 시작합니다.')
            time.sleep(2)
            option = self.options
            option.add_experimental_option('debuggerAddress','127.0.0.1:9222')
            
            cmd = ['chrome.exe', '--remote-debugging-port=9222', '--user-data-dir="C:\\Program Files\\Google\\Chrome\\Temp"']
            chrome_directory = 'C:\\Program Files\\Google\\Chrome\\Application'
            subprocess.run(cmd, cwd=chrome_directory, shell=True)

        else:
            self.browser.get(url)

    def find_ele(self, user_xpath):
        txt = self.browser.find_element(By.XPATH, user_xpath)
        action = ActionChains(self.browser)
        action.move_to_element(txt).perform()  
        return txt

    def find_ele_text(self,user_xpath):
        txt = self.find_ele(user_xpath)
        texts = txt.text.strip()
        print(texts)
        return texts

    def search_keyword(self,user_xpath, item_name):
        act = self.find_ele(user_xpath)
        act.send_keys(item_name)

    def click_button(self,button_xpath=None):
        try:
            button = self.find_ele(button_xpath)
            button.click()
            print('버튼 클릭 성공')
        except Exception as e:
            print('By.XPATH로 클릭되지 않습니다. By.PARTIAL_LINK_TEXT로 접근합니다! ')
            time.sleep(2)
            try:
                totext = self.find_ele_text(button_xpath)
                button = self.browser.find_element(By.PARTIAL_LINK_TEXT, totext)
                action = ActionChains(self.browser)
                action.move_to_element(button).perform()
                button.click() 
    
                print('성공!')
                if totext == None: 
                    print('해당 버튼의 키워드(이름)를 추가로 입력하세요. --> click_button(XPATH, 버튼 이름)')                    
            except Exception as e:
                print('문제발생!', type(e))

    def scroll_down(self, pixel=500, init_pos=False): 
        try:
            if init_pos == True:
                self.scroll_pos = 0         
            self.browser.execute_script(f"window.scrollTo({self.scroll_pos}, {self.scroll_pos+pixel})") 
            self.scroll_pos = self.scroll_pos + pixel 
            print('스크롤 다운 성공')
        except Exception as e:
            print('스크롤 다운 실패') 
            print(e)   
   
    def change_window(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def close_connect(self): 
        self.browser.close()
        print('finished.')
        print(' ')