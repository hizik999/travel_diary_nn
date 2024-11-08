from pydantic import BaseModel

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
        # Суммируем все значения полей, относящихся к показаниям датчиков, заглушка метод чтобы все работало
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

    def neural_network(self):
        self.label_id = 3 if self.total_sensor_value() > 0 else 0
        return self