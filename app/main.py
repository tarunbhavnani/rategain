from fastapi import FastAPI, Query
from app.flight_search import search_flights

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Travel Assistant API!"}


@app.get("/search-flights/")
async def search_flights_endpoint(
        origin: str = Query(..., description="Departure city"),
        originiD: str = Query(..., description="Departure city id"),
        destination: str = Query(..., description="Arrival city"),
        destinationiD: str = Query(..., description="Arrival city id"),
        departure_date: str = Query(..., description="Departure date YYYY-MM-DD"),
        return_date: str = Query(None, description="Return date YYYY-MM-DD (optional)")
):
    results = await search_flights(origin,originiD, destination, destinationiD, departure_date, return_date)
    return results
