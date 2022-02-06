from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from pymongo import MongoClient
from pydantic import BaseModel


class Reservation(BaseModel):
    name: str
    time: str
    table_number: int


client = MongoClient('mongodb://localhost', 27017)

db = client["restaurants-reservation"]
collection = db["reservation"]

app = FastAPI()


@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name: str):
    result = collection.find_one({"name": name}, {"_id": 0})
    if result:
        return {
            "status": "Found!",
            "result": result
        }
    else:
        return {"status": "Reservation not found."}


@app.get("/reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    result = collection.find({"table_number": table}, {"_id": 0})
    result_list = []
    for reservation in result:
        result_list.append(reservation)
    if result:
        return {
            "status": "Found!",
            "result": result_list
        }
    else:
        return {"status": "Reservation not found."}


@app.post("/reservation")
def reserve(reservation: Reservation):
    reservation = jsonable_encoder(reservation)
    collection.insert_one(reservation)
    return {"status": "Reservation created."}


@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    pass


@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number: int):
    pass
