#AREAS DE DIFERENETS FORMAS GEOMETRICAS
entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

pi = 3.14159



tri = (a * c ) / 2 
cir = (c * c) * pi 
tra = (a + b) * c / 2
qua = b * b 
ret = a * b

print (f'TRIANGULO: {tri:.3f}')
print (f'CIRCULO: {cir:.3f}')
print (f'TRAPEZIO: {tra:.3f}')
print (f'QUADRADO: {qua:.3f}')
print (f'RETANGULO: {ret:.3f}')
