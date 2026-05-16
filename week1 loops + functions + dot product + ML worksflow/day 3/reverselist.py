"""Create a list of 5 numbers.
Without using .reverse() —
loop through it backwards and
print each item.
Hint: use range(len(list)-1, -1, -1)"""

num = [1,2,3,4,5]
for i in range(len(num)-1,-1,-1) :
    print(num[i])
  