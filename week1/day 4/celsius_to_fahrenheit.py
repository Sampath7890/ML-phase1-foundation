"""Write convert(celsius) that returns Fahrenheit
Formula: F = (C × 9/5) + 32
Test: convert(0) → 32.0, convert(100) → 212.0, convert(37) → 98.6"""

def celsius_to_fahernheit(c) :
    return (c * 9/5) + 32
c = int(input("enter temp in celsius"))
print(celsius_to_fahernheit(c))

