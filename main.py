from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

class Reservation(BaseModel):
    name : str
    time: str
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
    reserve = collection.find_one({"time": reservation.time}, {"_id": 0})
    queue = {"table_number": reservation.table_number, 
             "name": reservation.name}
    new_time = { "$set": {"time": reservation.time} }
    if reserve is None:
        collection.update_many(queue, new_time)
        return {
            "status": "Updated"
        }
    return {
        "status": "Unfortunately, table is already reserved."
    }

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    reservation = {"name" : name, "table_number": table_number}
    collection.delete_one(reservation)
    return {
        "status": "Deleted"
    }
