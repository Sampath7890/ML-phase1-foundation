while True :
    def full_name(first,last) :
        first = first.capitalize()
        last = last.capitalize()

        return first + " " + last

    first = input("enter your first name: ")
    last = input("enter your last name : ")

    print(full_name(first,last))
