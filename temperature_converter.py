print()

def fetchTemperatureValue():
  print()
  temperature_value = float(input("Please input a value: "))
  return temperature_value

temperature_unit_valid = False
while temperature_unit_valid == False:
  temperature_unit = input("From Celcius or from Fahrenheit? [c/f]: ")
  if temperature_unit == "c":
    temperature_unit_valid = True
  elif temperature_unit == "f":
    temperature_unit_valid = True
  else:
    print("Please input a valid unit.\n")
    continue

if temperature_unit == "c":
  tempval = fetchTemperatureValue()
  converted_temperature = round(tempval*9/5 + 32, 2)
  print ("It's " + str(converted_temperature) + " degrees Fahrenheit.\n")
elif temperature_unit == "f":
  tempval = fetchTemperatureValue()
  converted_temperature = round((tempval - 32)*5/9, 2)
  print ("It's " + str(converted_temperature) + " degrees Celcius.\n")
