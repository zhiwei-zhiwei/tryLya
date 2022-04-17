from abc import ABC, abstractmethod
from serviceable import Serviceable

class CarFactory(ABC, serviceable):
    def needs_services(self):
        pass

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car = self.needs_services()