from MicroController import MicroControllerSettings

Standard_Program = MicroControllerSettings(8, 25, 40, 100, 37.5, 20, 100) #min_temp, max_temp, min_hum, max_hum, min_water_level, min_moist, max_moist
Winter_Program = MicroControllerSettings(0, 25, 40, 100, 37.5, 40, 100) #min_temp, max_temp, min_hum, max_hum, min_water_level, min_moist, max_moist
Summer_Program = MicroControllerSettings(15, 35, 20, 100, 37.5, 20, 100) #min_temp, max_temp, min_hum, max_hum, min_water_level, min_moist, max_moist

#sensor inputs:

#condition1
#current_moisture = 15
#current_temperature = 22
#current_humidity = 44
#current_water_level = 55

#condition2
#current_moisture = 15
#current_temperature = 22
#current_humidity = 39
#current_water_level = 55

#condition3
#current_moisture = 15
#current_temperature = 5
#current_humidity = 45
#current_water_level = 55

#condition4
#current_moisture = 18
#current_temperature = 32
#current_humidity = 41
#current_water_level = 55

#condition5
#current_moisture = 25
#current_temperature = 7
#current_humidity = 39
#current_water_level = 55

#condition63
#current_moisture = 26
#current_temperature = 10
#current_humidity = 45
#current_water_level = 55

#condition7
#current_moisture = 22
#current_temperature = 23
#current_humidity = 35
#current_water_level = 55

#condition8
#current_moisture = 25
#current_temperature = 27
#current_humidity = 37
#current_water_level = 55

#condition9
#current_moisture = 15
#current_temperature = 28
#current_humidity = 34
#current_water_level = 55

#condition10
#current_moisture = 5
#current_temperature = 22
#current_humidity = 39
#current_water_level = 55

#condition11
#current_moisture = 15
#current_temperature = 22
#current_humidity = 39
#current_water_level = 20

#condition12
current_moisture = 40
current_temperature = 22
current_humidity = 39
current_water_level = 55


print("The current mositure level is:", current_moisture, "%")
print("The current temperature is:", current_temperature, " degrees celsius")
print("The current humidity level is:", current_humidity, "%")
print("The current water level is:", current_water_level, "ml")

Standard_Program.calculate_moisture(current_moisture)
Standard_Program.calculate_temperature(current_temperature)
Standard_Program.calculate_humidity(current_humidity)
Standard_Program.calculate_water_level(current_water_level)

print(" \n Distribution (in ml): ", Standard_Program.calculate_water_distribution())

