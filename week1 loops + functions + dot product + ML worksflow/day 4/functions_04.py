def display_invoice(username , amount , due_date ) :
    print(f"hello ,{username}")
    print(f"your amount of ${amount} is due on {due_date}")

while True  :
    name = input("enter your name : ")
    amount = float(input("enter your amount: "))
    due_date = input("enter ur due date: ")

    display_invoice(name , amount , due_date)