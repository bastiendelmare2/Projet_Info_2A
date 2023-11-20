from fastapi import FastAPI, Path
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette import status
import uvicorn
from SERVICES.Service_stations import Service_Station
from BDD.DAO_StationsServices import StationsServices_Dao
from SERVICES.Service_compte import ServiceCompte

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
