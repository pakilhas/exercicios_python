entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

bas = b**2 - 4 * a * c
if bas >= 0:
	s1 = (-b + bas**0.5) / (2*a)
	s2 = (-b - bas**0.5) / (2*a)
	print(f"R1 = {s1:.5f}")
	#print(s2)
	print(f"r2 = {s2:.5f}")
elif bas < 0:
	print('deu errado')
else:
	('nada pra fazer')

#print(f"{s1} esse {s2}")
 
	
 
