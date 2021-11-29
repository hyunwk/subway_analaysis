import pandas as pd
from db_classes import Store
from db_connection import insert_article, insert_articles


def get_store():
    df = pd.read_csv('data/store.csv',  encoding='cp949').astype(object).replace(np.nan, 'None')
    # df = df.where(pd.notnull(df), None)
    articles = []
    # for row in df.itertuples():
    for row in df.dataframe():
        articles.append(Store(id=row[1],
                        store_type=row[2],
                        line=row[3],
                        name=row[4],
                        store_no=row[5],
                        square_meter=row[6],
                        start_date=row[7],
                        end_date=row[8],
                        price=row[10]
                        ))
    insert_articles(articles)
get_store()