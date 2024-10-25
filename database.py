import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DB_NAME')


class Connector:
    URL_DB = f'postgresql://{LOGIN}:{PASSWORD}@localhost/{DB_NAME}'

    def __init__(self):
        self.engine = create_engine(self.URL_DB)


    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def create_tables(self):
        try:

            print(f"Подключение к базе данных: {self.URL_DB}")
            Base.metadata.create_all(self.engine)

            print("Таблицы созданы")
        except Exception as e:
            print(f"Ошибка при создании таблиц: {str(e)}")


    def get_engine(self):
        return self.engine

