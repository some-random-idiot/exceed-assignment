from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

class Reservation(BaseModel):
    name : str
    time: int
    table_number: int
    
client = MongoClient('mongodb://localhost', 27017)

# TODO fill in database name
db = client["restaurants-reservation"]

# TODO fill in collection name
collection = db["reservation"]

app = FastAPI()


# TODO complete all endpoint.
@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name:str):
    pass

@app.get("reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    pass

@app.post("/reservation")
def reserve(reservation : Reservation):
    pass

@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    queue = collection.find_one({"table_number": reservation.table_number, 
                                 "time": reservation.new_time})
    if queue is None:
        return collection.update_one({"name": reservation.name, 
                                      "table_number": reservation.table_number}, 
                                      { "%set": {"time": reservation.new_time}
                                    })

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    reservation = {"name" : name, "table_namber": table_number}
    collection.delete_one(reservation)
