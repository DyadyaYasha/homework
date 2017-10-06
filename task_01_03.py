x = int(input())
y = int(input())
z = int(input())

l = [x, y, z]

for i in range(len(l)):
    l[i] = int(l[i])

n = 1

while n < len(l):
    for i in range(len(l)-n):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
    n += 1

for i in range(len(l)):
    l[i] = str(l[i])
    

print(', '.join(l))


