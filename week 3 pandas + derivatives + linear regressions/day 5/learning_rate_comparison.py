"""Run gradient descent 3 times on L(w) = w²
starting at w=8.0 for 20 steps each:
→ lr=0.01  (too slow)
→ lr=0.1   (just right)
→ lr=0.9   (too fast — might overshoot)

For each: print final w and final loss.
Which learning rate converged fastest?
Which one diverged (got worse)?
Print a conclusion line explaining why."""

import numpy as np
def gradient_descent(start , learning_rate , steps) :
    w = start 
    w_values = []
    loss_values = []

    for step in range(steps) :
        loss = w ** 2 
        derivative = 2 * w

        w_values.append(w)
        loss_values.append(loss)

        w = w - learning_rate * derivative

    return np.array(w_values)  , np.array(loss_values)   

learning_rates = [0.01 , 0.1 ,0.9]

for lr in learning_rates :
    w_array , loss_array = gradient_descent(8.0 , lr ,20)

    final_w = w_array[-1]
    final_loss = loss_array[-1]

    print(f"\nLearning Rate = {lr}")
    print(f"Final w = {final_w:.6f}")
    print(f"Final loss = {final_loss:.6f}")
