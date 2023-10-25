import requests

from fastapi import FastAPI

app = FastAPI()

@app.get("/import-data")
async def import_data(url: str):
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    app.run(debug=True)

data = import_data(https://donnees.roulezeco.fr/opendata/instantane)
