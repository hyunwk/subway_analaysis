import numpy as np
import pandas as pd
from db_classes import Store
from db_connection import insert_article, insert_articles


def get_store():
    whole_store = pd.read_csv('data/store.csv')
    store = pd.DataFrame(whole_store, columns=['store_name', 'start_date', 'end_date', 'rent_fee'])

    whole_transfer = pd.read_csv('data/transfer_info.csv')
    transfer = pd.DataFrame(whole_transfer, columns=['station_name', 'weekday', 'saturday', 'sunday'])

    whole_card_sep = pd.read_csv('data/CARD_SUBWAY_MONTH_202109.csv')

    #
    print(whole_card_sep.groupby('station_no')['get_on'].sum())
    # card_sep = pd.DataFrame(whole_card_sep.groupby('station_no'), columns=['date', 'line_no', 'station_no', 'get_on', 'get_off'])
    # print(card_sep)



get_store()
