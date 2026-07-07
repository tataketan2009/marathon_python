for i in range(0,11):
    print(i, end=" ")


i = 0
while i <= 10:
    print(i, end=" ")
    i += 1


for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=" ")


for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=" ")




l =  ['banana', 'orange', 'mango', 'lemon'] 

for l in reversed(l):
    print(l, end=" ")
