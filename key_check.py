# using this program to compare iso keys to ensure integrity
#input_1 is going to ask the user for the first key they want to compare against input_2
input_1 = input('Key 1: ')
#input_2 is going to ask the user for the second key they want to compare against input_1
input_2 = input('Key 2: ')

#here we will compare equality 
if input_1 == input_2:
    print('This is a safe image and can be used')
else:
    print('The keys do not match, please check again or download another image')
