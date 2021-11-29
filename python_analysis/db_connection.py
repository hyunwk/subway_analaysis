from typing import List

import pymysql

from sqlmodel import (
    create_engine, Session, SQLModel,
)

from db_classes import Store

server = 'localhost'
db_name = 'subway'
db_user = 'root'
db_pw = ''

engine = create_engine(
    f'mysql+pymysql://{db_user}:{db_pw}@127.0.0.1/{db_name}')

SQLModel.metadata.create_all(engine)

def insert_articles(articles):
    with Session(engine) as session:
        for article in articles:
            session.add(article)

        session.commit()

def insert_article(article:Store):
    with Session(engine) as session:
        session.add(article)
        session.commit()