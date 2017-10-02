#print('Введите три вершины')
#print('Введите координату X первой вершины')
vr1x = int(input())
#print('Введите координату Y первой вершины')
vr1y = int(input())
#print('Введите координату X второй вершины')
vr2x = int(input())
#print('Введите координату Y второй вершины')
vr2y = int(input())
#print('Введите координату X третьей вершины')
vr3x = int(input())
#print('Введите координату Y третьей вершины')
vr3y = int(input())

st1 = int((((vr1x - vr2x) ** 2) + ((vr1y - vr2y) ** 2)) ** 0.5)

st2 = int((((vr2x - vr3x) ** 2) + ((vr2y - vr3y) ** 2)) ** 0.5)

st3 = int((((vr3x - vr1x) ** 2) + ((vr3y - vr1y) ** 2)) ** 0.5)

if st1 > st2:
    m1 = st1
else: 
    m1 = st2
    
if st3 > m1:
    m1 = st3

if st1 < st2:
    m2 = st1
else:
    m2 = st2

if st3 < m2:
    m2 = st3

m3 = st1 + st2 + st3 - m1 - m2

if (m2 * m2) + (m3 * m3) == (m1 * m1):
    print('Прямоугольный')
else:
    print('Не прямоугольный')



