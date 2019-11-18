# This tool is to convert Farenheit to Celsius by asking the user to input the value in Fahrenheit and convert it to Celsius

x = float(input('Please enter the temperature in Fahrenheit'))
Celsius=round(((x-32)/1.8),2)
print (Celsius)