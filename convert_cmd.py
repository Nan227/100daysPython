import sys
import weather_i
print("* INFO: sys.argv==", sys.argv)

degC = float(sys.argv[1])

#print("* INFO: sys.argv==", degC)

print(weather_i.degF(degC))