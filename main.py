from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class SensorData(BaseModel):
    acceleration_x: float
    acceleration_y: float
    acceleration_z: float
    gyro_x: float
    gyro_y: float
    gyro_z: float
    magnetometer_x: float
    magnetometer_y: float
    magnetometer_z: float
    pressure: float
    label_id: int
    time: int
    id: int

    def total_sensor_value(self) -> float:
        # Суммируем все значения полей, относящихся к показаниям датчиков
        return (
            self.acceleration_x +
            self.acceleration_y +
            self.acceleration_z +
            self.gyro_x +
            self.gyro_y +
            self.gyro_z +
            self.magnetometer_x +
            self.magnetometer_y +
            self.magnetometer_z +
            self.pressure
        )

def neural_network(data: SensorData):
    data.label_id = 2 if data.total_sensor_value() > 0 else 0
    return data


@app.post("/")
def read_root(sensors: SensorData):
    return neural_network(sensors)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8081)
