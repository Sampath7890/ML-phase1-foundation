"""Create a list of 10 numbers.
Loop through and count how many are even
and how many are odd.
Print both counts."""

num = {1,2,3,4,5,6,7,8,9,10}
odd_count = 0
even_count = 0
for i in num :
    if i%2==0 :
        print(f"{i}=even")
        odd_count+=1
    else :
        print(f"{i}=odd")  
        even_count+=1
print("odd numbers = ",odd_count)
print("even numbwers = ",even_count)          
