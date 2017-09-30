print('Введите площадь садового участка в сотках ')
s = int(input())

s *= 100

gr = 15 * 25

if s < gr:
    print('Грядка не разбилась!')
else:
    while s:
        if s > gr:
            s -= gr
        elif s < gr:
            break
    print(int(s))


        


