s = int(input())
s *= 100
gr = 15 * 25

while s:
    if s > gr:
        s -= gr
    elif s < gr:
        break
print(int(s))

        


