#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_TYPE = os.getenv('DATABASE_TYPE')
ENGINE = os.getenv('ENGINE')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASS = os.getenv('DATABASE_PASS')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')

Base = declarative_base()

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = f'{DATABASE_TYPE}+{ENGINE}://'\
            f'{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
        
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_session(self):
        return self.__engine()

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        
    def check_db_structure(self):
    # Mapeando os modelos.
        Base.metadata.bind = self.__engine
        Base.metadata.create_all(self.__engine)
