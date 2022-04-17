from engine.engine import Engine

class WilloughbyEngine(Engine):
	def __init__(self, last_service_mileage, current_milage):
        super().__init__(last_service_mileage) = last_service_mileage;
        super().__init__(current_milage) = current_milage;
        
   	def needs_service(self):
   		service_threshold_mile = self.current_milage - self.last_service_mileage
        if service_threshold_mile > 60000:
            return True
        else:
            return False
