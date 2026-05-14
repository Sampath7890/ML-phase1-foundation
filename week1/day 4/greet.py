"""
Write greet(name, time_of_day="morning") with default parameter
greet("Sampath") → "Good morning, Sampath!"
greet("Rahul", "evening") → "Good evening, Rahul!"
greet("Priya", "night") → "Good night, Priya!"
"""
def greet(name , time_of_day="morning") :
    return print(f"good {time_of_day},{name}")
greet("sam","morning")
greet("ram")
greet("sita", "evening")