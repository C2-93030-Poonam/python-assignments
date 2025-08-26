#celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
 
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
  celsius = (fahrenheit - 32) * 5/9
  return celsius
   
celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")
print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")