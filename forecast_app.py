import weather_i

temp = [4.2, 1.5, 10.4]
#(variable) temp: list[float]
print("Today:            ",weather_i.degF(temp[0]))
print("Tomorrow:         ",weather_i.degF(temp[1]))
print("In next two days: ",weather_i.degF(temp[2]))
print(weather_i.degF(4.5))