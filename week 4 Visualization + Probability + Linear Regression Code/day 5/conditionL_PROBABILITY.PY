import numpy as np

print("\n--- Conditional Probability ---")
p_spam = 0.3
p_free_given_spam = 0.7
p_free_given_not_spam = 0.1
p_not_spam = 1 - p_spam

p_free = (p_free_given_spam * p_spam + p_free_given_not_spam * p_not_spam)
p_spam_given_free = (p_free_given_spam * p_spam) / p_free
print(f"P(spam | 'free'): {p_spam_given_free:.2f}")