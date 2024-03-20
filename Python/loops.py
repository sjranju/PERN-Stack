for i in range(1, 20, 2):
    print(i)

a = 5
while (a < 10):
    print(a)
    a += 1

print ('WHILE LOOP')
x = 1

while (x < 10):
    x += 1
    if(x == 4):
        continue
    print(x)

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
sum = 0

for i in arr1:
    for j in arr2:
        sum += i+j
print('Sum:',sum)