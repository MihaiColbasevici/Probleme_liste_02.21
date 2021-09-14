temp = []
for i in range(0, 24):
    i = int(input('> '))
    temp.append(i)
# a)
print('Temperatura medie: ', sum(temp) / len(temp))
# b)
print('Maximul °: ', max(temp), ';', ' Minimul °: ', min(temp))
# c)
maxt = max(temp)
maxtemp = []
for k, j in enumerate(temp):
    if j == maxt:
        maxtemp.append(k)
print('Temperatura maximă a fost înregistrată la ora (orele): ', *maxtemp)
# d)
mint = min(temp)
mintemp = []
for l, h in enumerate(temp):
    if h == mint:
        mintemp.append(l)
print('Temperatura minimă a fost înregistrată la ora (orele): ', *mintemp)