n = int(input())
p = int(input())

with open('data.txt') as f:
    ryad = f.read().split(' ')

with open('out-1.txt', 'w') as dele:
    d = []
    for i in ryad:
        if int(i) % n == 0:
            d.append(i)
    dele.write(' '.join(d))

with open('out-2.txt', 'w') as step:
    s = []
    for i in ryad:
        vz = int(i) ** p
        s.append(str(vz))
    step.write(' '.join(s))