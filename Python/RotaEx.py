#!/usr/bin/python
# -- encoding: utf-8 --
import sys
import logging
import uvicorn

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from ConexãoBDEx import DBConnectionHandler
from ModelosEx import Tb_order
from typing import List
from EsquemasEx import OrderSchema

logger = logging.getLogger(__name__)
app = FastAPI()

# Rotas.
@app.get("/orders/{id}", response_model=OrderSchema)
def get_order(id: int):
    with DBConnectionHandler() as db:
        order = db.session.query(Tb_order).filter(Tb_order.pk_order == id).first()
        if order:
            return order
        else:
            raise HTTPException(status_code=404, detail=f"Order with ID {id} not found.")

@app.get("/orders", response_model=List[OrderSchema])
def list_orders(skip: int = 0, limit: int = 10):
    with DBConnectionHandler() as db:
        orders = db.session.query(Tb_order).offset(skip).limit(limit).all()
        return orders

@app.post("/orders", response_model=OrderSchema)
def create_order(order: OrderSchema):
    with DBConnectionHandler() as db:
        new_order = Tb_order(**order.model_dump())
        db.session.add(new_order)
        db.session.commit()
        db.session.refresh(new_order)
        return new_order

@app.put("/orders/{id}", response_model=OrderSchema)
def update_order(id: int, order: OrderSchema):
    with DBConnectionHandler() as db:
        db_order = db.session.query(Tb_order).filter(Tb_order.pk_order == id).first()
        if db_order:
            for key, value in order.model_dump().items():
                setattr(db_order, key, value)
            db.session.commit()
            db.session.refresh(db_order)
            return db_order
        else:
            raise HTTPException(status_code=404, detail=f"Order with ID {id} not found.")

@app.delete("/orders/{id}", status_code=204)
def delete_order(id: int):
    with DBConnectionHandler() as db:
        db_order = db.session.query(Tb_order).filter(Tb_order.pk_order == id).first()
        if db_order:
            db.session.delete(db_order)
            db.session.commit()
            return
        else:
            raise HTTPException(status_code=404, detail=f"Order with ID {id} not found.")
        
if __name__ == '__main__':

    # identificação de migrations
    if 'makemigrations' in sys.argv:
        with DBConnectionHandler() as db:
            db.check_db_structure()
            sys.exit()


    uvicorn.run('app:app', host="0.0.0.0", port=8000, log_config='./logging.conf.yml', reload=True)