import math

entrada = input().split()
x1 = float(entrada[0])
y1 = float(entrada[1])

entrada = input().split()
x2 = float(entrada[0])
y2 = float(entrada[1])

d = math.sqrt(((x2 - x1) *  (x2-x1)) + ((y2 - y1) * (y2 - y1)))

print (f'{d:.4f}')
