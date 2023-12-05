tempo = int(input())

hor = tempo // 3600
min = (tempo % 3600) // 60
seg = tempo % 60

print(f'{hor}:{min}:{seg}')



