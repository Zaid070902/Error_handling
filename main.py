try:
    x = 1/0
    print("Dividing 1 by zero.")
except ZeroDivisionError:
    print("You can not divide by zero!")
finally:
    print("I will always run, no matter what!")
