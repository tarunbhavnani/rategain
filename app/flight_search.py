import httpx
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")


async def search_flights(origin,originId, destination,destinationId, departure_date, return_date=None):
    url = "https://skyscanner89.p.rapidapi.com/flights/one-way/list"

    params = {
        "adults": "1",
        "origin": origin,
        "originId": originId,

        "destination": destination,
        "destinationId": destinationId,
        "departureDate": departure_date,
        "returnDate": return_date,
        "currency": "USD"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()

    # Return raw response for now (we'll pretty it later)
    return data