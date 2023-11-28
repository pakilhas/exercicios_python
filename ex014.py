entrada = input().split()
cod1 = int(entrada[0])
n1 = int(entrada[1])
v1 = float(entrada[2])

entrada = input().split()
cod2 = int(entrada[0])
n2 = int(entrada[1])
v2 = float(entrada[2])

vt = (n1 * v1)  + (n2 * v2) 

print(f'VALOR A PAGAR: R$ {vt:.2f}') 
