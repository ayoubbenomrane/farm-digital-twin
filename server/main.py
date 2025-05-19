from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# CORS to allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ORION_URL = "http://localhost:1026/v2/entities"

@app.get("/parcels")
async def get_all_parcels():
    async with httpx.AsyncClient() as client:
        res = await client.get(ORION_URL + "?type=Parcel")
        return res.json()
