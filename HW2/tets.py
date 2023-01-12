count_bilet = int(input('Введите количество билетов: '))
massiv = {}
cost = []
for i in range(count_bilet):
    massiv[i] = int(input('Введите возраст: '))
    if massiv.get(i) < 18:
        cost.append(0)
        print("Цена билета: 0")
    elif 18 <= massiv.get(i) < 25:
        cost.append(990)
        print("Цена билета: 990")
    elif 25 <= massiv.get(i):
        cost.append(1390)
        print("Цена билета: 1390")
if count_bilet > 3:
    discount = sum(cost) - (sum(cost) * 0.1)
    print ("Итого к оплате: ", discount)
else:
    print("Итого к оплате: ", sum(cost))

    
    
    
    
    




