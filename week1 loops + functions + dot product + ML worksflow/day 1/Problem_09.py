"""
A bank offers 7% simple interest per year. Take principal amount 
and number of years as input. Print the interest earned and total amount.
"""

principal = int(input("enter principal amount: "))
tenure = int(input("enter number pf years: "))

simple_intrest = (principal * 7 * tenure)/100
print(f"simpleintrest : {simple_intrest}")
print(f"total amount will be payed : {simple_intrest + principal}")