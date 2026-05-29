"""
Write a function numerical_derivative(f, x, h=0.0001):
→ Uses the formula: (f(x+h) - f(x)) / h
→ This approximates the derivative at point x


Test with:
- f(x) = x²  at x=3 → should be close to 6
- f(x) = 3x  at x=5 → should be close to 3
- f(x) = x³  at x=2 → should be close to 12


Print each result with 4 decimal places.
This is how computers actually calculate derivatives.

"""

def numerical_derivative(f, x, h=0.0001):
    return  ((f(x+h) - f(x)) / h)

result1 = numerical_derivative(lambda x : x**2 ,3 )
result2 = numerical_derivative(lambda x : 3*x ,5 )
result3 = numerical_derivative(lambda x : x**3 ,2 )

print(f"f(x) = x² at x = 3 : {result1:.4f}")
print(f"f(x) = 3x at x = 5 : {result2:.4f}")
print(f"f(x) = x³ at x = 2 : {result3:.4f}")
