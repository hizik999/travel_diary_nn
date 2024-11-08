from fastapi import FastAPI
import uvicorn
from models import SensorData

app = FastAPI()


@app.post("/")
def read_root(sensors: SensorData):
    return sensors.neural_network()



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8081)
