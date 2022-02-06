from unicodedata import name
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

class Reservation(BaseModel):
    name : str
    time: int
    table_number: int
    
client = MongoClient('mongodb://localhost', 27017)

# TODO fill in database name
db = client["restaurant"]

# TODO fill in collection name
collection = db["reservatoin"]

app = FastAPI()

def check_table_availability(time: int, table: int) -> bool:
    result = collection.find({"time": time, "table_number": table})
    list_cursor = list(result)
    return not len(list_cursor) > 0

# TODO complete all endpoint.
@app.get("/reservation/by-name/{name}")
def get_reservation_by_name(name:str):
    pass

@app.get("reservation/by-table/{table}")
def get_reservation_by_table(table: int):
    pass

@app.post("/reservation")
def reserve(reservation : Reservation):

    if not check_table_availability(reservation.time, reservation.table_number):
        # Incase that the reservation is found based on the condition above
        raise HTTPException(status_code=400, detail={
            "message": "That table isn't available at that time"
        })
    # Insert new data
    insert_result = collection.insert_one({
        "name": reservation.name,
        "time": reservation.time,
        "table_number": reservation.table_number
    })
    # Return response
    return {
        "message": "success",
        "id": str(insert_result.inserted_id)
    }

@app.put("/reservation/update/")
def update_reservation(reservation: Reservation):
    pass 

@app.delete("/reservation/delete/{name}/{table_number}")
def cancel_reservation(name: str, table_number : int):
    query = {
        "name":name , 
        "table_number":table_number
         }
    reservation.delete_one(query)
    return {}
    
