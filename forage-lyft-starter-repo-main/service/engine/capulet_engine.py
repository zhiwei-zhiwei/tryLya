from abc import ABC

from service.car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = current_mileage - last_service_date;

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000
