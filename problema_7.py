v = []
for i in range(0, 7):
    k = int(input('> '))
    v.append(k)
print('Venitul săptămânal: ', sum(v))
print('Media venitului zilnic: ', (sum(v) / len(v)))
print('Ziua în care s-a obținut cel mai mare venit: ', max(v))
print('Ziua în care s-a obținut cel mai mic venit: ', min(v))