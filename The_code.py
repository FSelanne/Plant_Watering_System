class MicroControllerSettings:
  
    def __init__(self, min_temp, max_temp, min_hum, max_hum, min_water_level, min_moist, max_moist):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.min_hum = min_hum
        self.max_hum = max_hum
        self.min_water_level = min_water_level
        self.min_moist = min_moist
        self.max_moist = max_moist
        self.moisture_needed = False
        self.temperature_optimal = False
        self.water_needed = False
        self.humidity_optimal = False
        self.moisture_sub_optimal = False
        self.current_temp_not_optimal = False
        self.current_humidity_not_optimal = False
        self.death_imminent = False
        self.danger_moist = 10

    def calculate_moisture(self, current_moisture):
        if current_moisture <= self.min_moist:
            self.moisture_needed = True
        elif self.min_moist <= current_moisture <= self.max_moist:
            self.moisture_sub_optimal = True
        if current_moisture <= self.danger_moist:
            self.death_imminent = True

    def calculate_temperature(self, current_temperature):
        if self.min_temp <= current_temperature <= self.max_temp:
            self.temperature_optimal = True
        if current_temperature in range((self.min_temp-2), (self.min_temp+3)) or current_temperature in range((self.max_temp-2), (self.max_temp+3)):
            self.current_temp_not_optimal = True

    def calculate_water_level(self, current_water_level):
        if self.min_water_level > current_water_level:
            self.water_needed = True

    def calculate_humidity(self, current_humidity):
        if self.min_hum <= current_humidity <= self.max_hum:
            self.humidity_optimal = True
        if current_humidity in range((self.min_hum-5), (self.max_hum+6)):
            self.current_humidity_not_optimal = True


    def calculate_water_distribution(self):
        distribution = 0
        if self.water_needed == False:
            if self.moisture_needed and self.temperature_optimal and self.humidity_optimal:
                distribution = 25 #C1
            if self.moisture_needed and self.temperature_optimal and self.humidity_optimal == False:
                distribution = 12.5 #C2
            if self.moisture_needed and self.temperature_optimal == False and self.humidity_optimal:
                distribution = 12.5 #C3
            if self.moisture_sub_optimal and self.current_temp_not_optimal and self.current_humidity_not_optimal:
                distribution = 12.5 #C4
            if self.death_imminent == True:
                distribution = 37.5 #C5
            
        else:
            distribution = "Water level is not sufficient enough. Please refill."
        if distribution == 0:
            distribution = "0 - The plant should not be watered"

        return distribution  # "The system will output %i mm of water" % distribution   
        
