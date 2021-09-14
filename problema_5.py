x = []
y = []
for i in range(0, 5):
    k = int(input('> '))
    x.append(k)
y = x
print('Suma primelor 3 elemente: ', x[0] + x[1] + x[2])
print('Suma: ', sum(y))
prod = 1
for j in range(len(x)):
    prod *= x[j]
print('Produsul: ', prod)
print('Modulul elementului 3: ', abs(y[2]))
print('Suma primelor elemente: ', x[0] + y[0])