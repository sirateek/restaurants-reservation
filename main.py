from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

class Reservation(BaseModel):
    name : str
    time: int
    table_number: int
    
client = MongoClient('mongodb://localhost', 27017)

# TODO fill in database name
db = client["restaurant"]

# TODO fill in collection name
collection = db["reservation"]
menu_collection=db["reservation"]

app = FastAPI()

# TODO complete all endpoint.
@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name:str):
    query={"name":name}
    query_result=menu_collection.find(query)
    for n in query_result:
        print(n)

@app.get("reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    query={"table_number":table}
    query_result=menu_collection.find(query)
    for n in query_result:
        print(n)

@app.post("/reservation")
def reserve(reservation : Reservation):
    pass

@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    pass

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    pass

