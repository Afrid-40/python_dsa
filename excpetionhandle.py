x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
try:
    print(x/y)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    print("done")