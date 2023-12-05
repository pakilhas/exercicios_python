#PROGRAMA PARA SABER QUAL MAIOR NUMERO
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorab = (a + b + abs (a - b) ) /2
maiorabc = (maiorab + c + abs (maiorab - c)) /2 
print(f'{maiorabc:.0f} eh o maior')
