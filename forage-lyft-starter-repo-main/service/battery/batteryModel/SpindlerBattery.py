from battery.battery import Battery

class SpindlerBattery(Battery, last_service_date, current_data):
	def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date) = last_service_date;
        
   	def needs_service(self):
   		service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

