# this is to learn about for loops 
import random
list_1=['!','@','#','$','%','&']
list_2=['1','2','3','4','5','6','7','8','9','0','a','A','b','B','c','C','d','D','e','E','f','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']

for tup1 in random.choice(list_1):
	for tup2 in random.choice(list_2):
		for tup3 in random.choice(list_2):
			for tup4 in random.choice(list_2):
				for tup5 in random.choice(list_2):
					for tup6 in random.choice(list_2):
						for tup7 in random.choice(list_2):
							for tup8 in random.choice(list_2):
								print(tup1+tup2+tup3+tup4+tup5+tup6+tup7+tup8)


	