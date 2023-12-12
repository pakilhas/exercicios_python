entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

bas = b**2 - 4 * a * c
if a == 0:
	print('Impossivel calcular')
else:
 if bas >= 0:
  s1 = (-b + bas**0.5) / (2*a)
  s2 = (-b - bas**0.5) / (2*a)
  print(f"R1 = {s1:.5f}")
  print(f"R2 = {s2:.5f}")

 else:
  print("Impossivel calcular")
