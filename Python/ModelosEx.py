#!/usr/bin/python
# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, Float, Table, Date, Boolean
from ConexãoBDEx import Base

class User(Base):
    __tablename__ = 'User'
 
    pk_user = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(Text)
    email = Column(String(50))
    cep = Column(Integer)
    city = Column(String(25))
    address = Column(String(30))
    neighborhood = Column(String(30))
    cellphone = Column(String(25))
    user_token = Column(String(16))
    is_active = Column(Boolean, nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    is_employee = Column(Boolean, nullable=False)
 
class Tb_product (Base):
    __tablename__ = 'Tb_product'
 
    pk_produto = Column(Integer, primary_key=True)
    name = Column(String(50))
    descricao = Column(Text)
    value = Column(Float)
    quanty = Column(Integer)
    
class Tb_cart(Base):

    __tablename__ = 'Tb_cart'
    
    pk_cart = Column(Integer, primary_key=True)
    fk_user = Column(String(50))
    fk_product = Column(Text)
    quantity = Column(Float)
    
class Tb_authentication(Base):

    __tablename__ = 'Tb_authentication'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    access_token = Column(Text)
    expiration = Column(Date)
    
class Tb_order(Base):
    __tablename__ = 'Tb_order'
    
    pk_order = Column(Integer, primary_key=True)
    fk_user = Column(String(50))
    fk_product = Column(Text)
    quantity = Column(Float)
    order_number = Column (Integer)
    
class Tb_payment(Base):
    __tablename__ = 'Tb_payment'
    
    pk_payment = Column(Integer, primary_key=True)
    fk_order = Column(Integer)
    city = Column(String(50))
    address = Column(Text)
    neighborhood = Column(String(30))
    country = Column(String(30))
    fk_send = Column(Integer)
    fk_payment_type = Column(Integer)
    value = Column(Integer)
    card_name = Column(Text)
    card_number = Column(String(30))
    data_expiration = Column(Date)
    
class Tb_send_type(Base):
    __tablename__ = 'Tb_send_type'
    
    pk_send = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(Text)
    email = Column(String(50))
    cep = Column(Integer)
    cidade = Column(String(50))
    logradouro = Column(String(50))
    bairro = Column(String(50))
    telefone = Column(String(50))
    descricao = Column(Text)
    
class Tb_payment_type(Base):
    __tablename__ = 'Tb_payment_type'
    
    pk_send = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    type = Column(Integer)