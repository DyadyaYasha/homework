vr1x = int(input())
vr1y = int(input())
vr2x = int(input())
vr2y = int(input())
vr3x = int(input())
vr3y = int(input())

st1 = ((vr1x - vr2x) ** 2 + (vr1y - vr2y) ** 2)

st2 = ((vr2x - vr3x) ** 2 + (vr2y - vr3y) ** 2)

st3 = ((vr3x - vr1x) ** 2 + (vr3y - vr1y) ** 2)

if st1 > st2 and st1 > st3:
    m3 = st1
    m1 = st2
    m2 = st3

elif st2 > st1 and st2 > st3:
    m3 = st2
    m1 = st1
    m3 = st3
elif st3 > st1 and st3 > st2:
    m3 = st3
    m1 = st1
    m2 = st2

if m1 + m2 == m3:
    print('Прямоугольный')
else:
    print('Не прямоугольный')



