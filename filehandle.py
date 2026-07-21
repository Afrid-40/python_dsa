with open("file.txt", "w") as file:                 #12th test-run
    file.write("hello world")
with open("file.txt", "r") as file:
    print(file.read())
with open("file.txt", "a") as file:
    file.write("\nMugiwara no Luffy")
with open("file.txt", "r") as file:
    print(file.read())