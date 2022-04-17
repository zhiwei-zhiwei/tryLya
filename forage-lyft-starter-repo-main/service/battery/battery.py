from service.car import Car

class Battery(Car):
	def needs_services(self):
        return datetime.today().date() - self.last_service_date.date();

