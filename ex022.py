#CALCULAR CEDULAS DE UM VALOR
val = int(input())

ceds = [100, 50, 20, 10, 5, 2, 1]

print(val)

for ced in ceds:
	qtd_ced = val // ced
	val %= ced
	print(f'{qtd_ced} nota(s) de R$ {ced},00')
