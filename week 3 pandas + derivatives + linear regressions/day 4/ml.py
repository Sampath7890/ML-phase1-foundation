# House price example

weight = 4
size = 2
actual = 10
learning_rate = 0.1

for step in range(5):

    prediction = weight * size

    loss = (prediction - actual) ** 2

    derivative = 2 * (prediction - actual) * size

    weight = weight - learning_rate * derivative

    print("Step:", step)
    print("Prediction:", prediction)
    print("Loss:", loss)
    print("Weight:", weight)
    print()