"""Write is_even(n) that returns True or False
is_even(4) → True, is_even(7) → False
Then write is_odd(n) that CALLS is_even — don't rewrite the logic"""

def is_even(n) :
    return n%2==0
def is_odd(n) :
    return not is_even(n)

n=int(input("enter a number: "))

print(f"even = {is_even(n)}")
print(f"odd = {is_odd(n)}")
