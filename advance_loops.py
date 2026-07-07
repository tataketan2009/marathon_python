#this way is very long
l = range(0, 101)

even = []
odd = []


for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(sum(even))
print(sum(odd))

#this way is more advanced

sum_even = sum(range(0, 101, 2))
sum_odd = sum(range(1, 101, 2)) 

print(sum_even)
print(sum_odd)