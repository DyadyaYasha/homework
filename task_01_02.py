#print('Сколько у вас тарелок?')

tar = int(input())

#print('А сколько у вас моющего средства?')

ms = float(input())


while tar:

    if tar > 0:
        tar -= 1
        ms -= 0.5

    if ms == 0:
        break
    
    if tar == 0:
        break

if tar == 0:
    if ms == 0:
        print('Все тарелки вымыты, моющее средство закончилось')

    else:

        print('Все тарелки вымыты. Осталось', ms, 'ед. моющего средства')

elif ms == 0:
    print('Моющее средство закончилось. Осталось', tar, 'тарелок')