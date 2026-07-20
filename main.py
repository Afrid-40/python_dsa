print("Luffy\n luffy1")                         #1st tes-run
print("\t current\\new\\folder")                # 2nd test-run
# / is escape character

print('------------------------------------------------------------------------')

print(r"\tcurrent\new\folder")                  # 3rd test-run

print('------------------------------------------------------------------------')

# function to check odd or even
def odd_even():                                 #4th test-run
    input_num = int(input("Enter a number: "))
    if input_num % 2 == 0:
        print("even")
    else:
        print("odd")

odd_even()

print('------------------------------------------------------------------------')


l=[1,2,3,4,5,6,7,8,9,10]                            #5th test-run
print(l[0:5])                      
l.pop()                   # prints first 5 elements
print(l)
print('------------------------------------------------------------------------')
dict={                                                                  #6th test-run
    "name":"luffy",
    "gender":"male",
    "age":20,
    "crew_members": ["zoro", "nami", "usopp", "sanji", "chopper", "robin", "franky", "brook"]
}
print(dict)

print('------------------------------------------------------------------------')

dict["age"]=21          #to update the value of age
print(dict)

dict.update({"name":"Mugiwara <:"})    #to update the value of name
print(dict)

print(dict)                             #printing the dictionary    
print(dict.get("name"))                 #printing the value of name key
print(dict.keys())                      #pritning the keys of the dictionary
print(dict.values())                    #printing the values of the dictionary
print(dict.items())                     #printing the items of the dictionary

print('------------------------------------------------------------------------')

def count(*args):                                 #7th test-run
    print(type(args))                               #to check the type of args
count(1,2,3,4,5,6,7,8,9,10)                         #calling the function
print('------------------------------------------------------------------------')
def dict(**kwargs):                                 #8th test-run
    print(type(kwargs))                               #to check the type of kwargs
dict(name="luffy", age=20, gender="male")               #calling the function
print('------------------------------------------------------------------------')


def default(gender="male", age=20, name="luffy"):                                 #9th test-run
    print(f"Name: {name}, Age: {age}, Gender: {gender}")

default()                                 #calling the function
print('------------------------------------------------------------------------')

#OOPS concepts

l=[1,2,3,4,5,6,7,8,9,10]                            #10th test-run
s = "string"
len(l)                       #to get the length of list
len(s)                       #to get the length of string
print(len(l))
print(len(s))


                                            # 4-Pillars of OOPS 
                                            # 1. Encapsulation
                                            # 2. Abstraction
                                            # 3. Inheritance
                                            # 4. Polymorphism

x=10
x="gaban"                    #dynamic typing
print('------------------------------------------------------------------------')


s = input("Enter a string: ")               #11th test-run
print(s[1:-1])
print(s[::-1])
print(s[1::])

print('-----------------------------------------------------------------------')

#take a number as input and find the sum of nnumbers from 1 to that number
n = int(input("Enter a number:"))
sum = 0
for i in (1, n + 1):
    sum += i
print("The sum is:", sum)