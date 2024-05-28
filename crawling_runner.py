from crawlingDB.helpers.crawling_hyundai import get_hyundai
from crawlingDB.helpers.crawling_kia import get_kia
from crawlingDB.helpers.crawling_genesis import get_genesis


if __name__ == '__main__':
    hyundai_df= get_hyundai()
    genesis_df = get_genesis()
    kia_df = get_kia()



