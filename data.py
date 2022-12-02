#The data file

#----Unit testing-----------------------------------------------------------------------

#Condition 1 (optimal conditions for watering)
current_moisture = 15
current_temperature = 22
current_humidity = 44
current_water_level = 55
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 1:")
print(Standard_Program.calculate_water_distribution())

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100)

#Condition 2 (non optimal humidity)
current_moisture = 15
current_temperature = 22
current_humidity = 39
current_water_level = 55
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 2:")
print(Standard_Program.calculate_water_distribution())

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100)

#Condition 3 (non optimal temp)
current_moisture = 15
current_temperature = 5
current_humidity = 45
current_water_level = 55
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 3:")
print(Standard_Program.calculate_water_distribution())

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100)

#Condition 4 (pre-emptive - to prevent worst case scenario - before it goes too bad)
current_moisture = 25
current_temperature = 7
current_humidity = 39
current_water_level = 55
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 4:")
print(Standard_Program.calculate_water_distribution())

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100)

#Condition 5 ( moisture lower than 10%)
current_moisture = 5
current_temperature = 22
current_humidity = 39
current_water_level = 55
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 5:")
print(Standard_Program.calculate_water_distribution())

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100)

#Condition 6 (water barrel less than 37.5mm water)
current_moisture = 15
current_temperature = 22
current_humidity = 39
current_water_level = 20
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 6:")
print(Standard_Program.calculate_water_distribution())

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100)

#Condition 7 (plant is happy)
current_moisture = 40
current_temperature = 22
current_humidity = 39
current_water_level = 55
Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_water_level(current_water_level)
print("Condition 7:")
print(Standard_Program.calculate_water_distribution())

