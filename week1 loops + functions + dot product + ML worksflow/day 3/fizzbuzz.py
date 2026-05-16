"""FizzBuzz — the classic
Print numbers 1 to 50.
Multiple of 3 → print "Fizz"
Multiple of 5 → print "Buzz"
Multiple of both → print "FizzBuzz"
Otherwise → print the number"""

for i in range(50) :
    print(i)
    if i % 3 == 0 and i % 5 == 0 :
        print(f"{i}.fizzbuzz")  
    elif i % 3 == 0 :
        print(f"{i}.fizz")
    elif i % 5 == 0 :
        print(f"{i}.buzz")    
    elif i % 3 == 0 and i % 5 == 0 :
        print(f"{i}.fizzbuzz") 
    else :
        print(i)      