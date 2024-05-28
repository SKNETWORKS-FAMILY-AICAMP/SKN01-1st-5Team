# SKN01-1st-5Team
<div align="center">
<img width="600" alt="image" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/7ea63fc3-95f0-44d5-a0f0-cf431cae34f1">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-1st-5Team&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

# 통합 FAQ 조회 시스템
> **SK Networks AI CAMP 1기** <br/> **개발기간: 2024.05.27 ~ 2024.05.28** 

## 개발팀 소개

| 김용현 | 정아람 | 최민지 | 한재혁 |
|:----------:|:----------:|:----------:|:----------:|
| <img width="120px" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/33ea2a85-1853-484b-b2a4-c750f854a26b" /> | <img width="120px" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/b24cae67-75d6-48aa-a94e-e847a769f2c0" /> | <img width="120px" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/a3b96d0b-7537-4670-afaa-57279dab5552" /> |  <img width="120px" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/036ed196-ea34-45d8-bc47-58d84c9927c9" /> |
| [@younghyen7956](https://github.com/younghyen7956) | [@Ah-ram](https://github.com/Ah-ram) | [@Minn-ji](https://github.com/Minn-ji) | [@Jh-jaehyuk](https://github.com/Jh-jaehyuk) |
| 학교 + 학과 or Something else | 학교 + 학과 or Something else | 학교 + 학과 or Something else | 학교 + 학과 or Something else  |

## 프로젝트 개요 및 소개
최근 우리나라는 자동차 산업의 수출액 증가로 인한 경제 성장과 교외 지역으로 이동하는 인구가 증가함에 따라 차량 대수가 증가하고 있습니다. 그러나, 증가하는 차량 대수와는 다르게 차량에 대한 정보를 얻는 것은 

## 시작 가이드
### Requirements
For building and running the application you need:

- [MariaDB 10.4.34](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.4.34) or [MySQL 8.0.37](https://dev.mysql.com/downloads/installer/)
- [Python >= 3.11.7](https://www.python.org/downloads/release/python-3119/)

### Installation
``` bash
$ git clone https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-1st-5Team.git
$ cd SKN01-1st-5Team
$ pip install -r requirements.txt
```
---
## Stacks :books:

### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Development
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

### Communication
![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)

## 화면 구성 📺
| 메인 페이지  |  페이지1을 소개하는 이름 | 페이지2를 소개하는 이름  |
| :----------------------------------: | :------------: |   :------------:  |
| 홈 사진 |  페이지1  | 페이지2 |

---
## 기능 소개 📦

### 페이지 1에서 제공하는 기능
 - 선택한 지역의 연도별 차량 등록 현황을 그래프로 제공합니다.
### 페이지 2에서 제공하는 기능
 - 국내 점유율 상위 3개 브랜드 FAQ를 통합 검색할 수 있는 기능을 제공합니다.

---
## 아키텍처

### 디렉토리 구조
```bash
.
├── README.md
├── crawlingDB
│   └── helpers
│       ├── base
│       │   └── crawling_sele.py
│       ├── connectTB.py
│       ├── crawling_genesis.py
│       ├── crawling_hyundai.py
│       ├── crawling_kia.py
│       └── make_brandTB.py
├── crawling_runner.py
├── csv_to_db.py
├── getQuery.py
├── makeDB_runner.py
├── result
│   ├── total_genesis.csv
│   └── total_kia.csv
├── runner.py
└── source
    ├── home.py
    ├── make_csv.py
    ├── multiapp.py
    ├── page1.py
    ├── page2.py
    ├── requirements.txt
    └── runner.py
```

