from service.car import Car

class Engin(Car):
	def needs_services(self):
        return self.current_mileage - self.last_service_mileage