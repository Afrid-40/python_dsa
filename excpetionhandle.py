# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("done")


for i in range(5):
    print(i)
    if i==4:
        break
        print(i)
else:
    print("done")


try:
    a = int(input("enter a number:"))
    print(a)
except ValueError as e:
    print(e)    
else: 
    print("done")