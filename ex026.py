#converter notas em moedas
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
	qt_notas = valor // nota
	valor %= nota
	print(f"{qt_notas:.0f} nota(s) de R$ {nota:.2f}")
print("MOEDAS:")
for moeda in moedas: 
	qt_moedas = valor // moeda
	valor %= moeda
	print(f"{qt_moedas:.0f} moeda(s) de R$ {moeda:.2f}")

