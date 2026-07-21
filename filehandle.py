with open("file.txt", "w") as file:                 #12th test-run
    file.write("hello world")
with open("file.txt", "r") as file:
    print(file.read())
with open("file.txt", "a") as file:
    file.write("\nMugiwara no Luffy")
with open("file.txt", "r") as file:
    print(file.read())

#task1
## keep asking valid integer number
## if not valid integer number, print error
while True:
    try:
        num = int(input("enter a number: "))
        print("it is a valid number")
        break
    except ValueError:
        print("Error: not a valid number , give a valid number")


# task2 
## handle index error while accessing list elements if it is our of range handle it 
l=[1,2,3,4,5,6,7,8,9,10]
try:
    print(l[10])
except IndexError as e:
    print(e)

#apprach 2 for task2

l=[1,2,3,4,5,6,7,8,9,10]
try:
    index = int(input("give an index :"))
    print(l[index])
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)