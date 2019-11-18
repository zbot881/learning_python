# This tool is to convert the temperature by asking the user which measure the user wants to convert input_1. 
# Then asking the user to input the value to convert (Fahrenheit/Celsius).
# If input received is different than 1 or 2 and Invalid Input message will appear
# Result will be the converted value (Fahrenheit/Celsius)

input_1=int(input('Select value to convert \n1-Celsius \n2-Fahrenheit \n'))

if input_1 == 1:
	x = float(input('Please enter the temperature in Celsius '))
	Fahrenheit=round((x*1.8+32),2)
	print(Fahrenheit)
elif input_1 == 2:
	x = float(input('Please enter the temperature in Fahrenheit '))
	Celsius=round(((x-32)/1.8),2)
	print(Celsius)
else:
	print('Invalid Input')
