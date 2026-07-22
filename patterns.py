from unicodedata import digit


n=5
for i in range(n):
    for j in range(n):
        print("*", end= " ")
    print()
#RIGHT ANGLED TRIANGLE
print("----------------------------------------------------")
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end= " ")
    print()
    
print("----------------------------------------------------")
# inverted right angled traingle
n = 5
for i in range(n, 0, -1):
    print('*' * i)

print("----------------------------------------------------")

# diamond pattern
n =5
 
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()

for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

print("----------------------------------------------------")


# Armstrong number
n=int(input("Enter number: "))
order=len(str(n))
s=0
t=n
while t>0:
    d=t%10
    s+=d ** order
    t//=10
if n==s:
    print(n)
else:
    print("Not an armstrong number")
print("----------------------------------------------------")

#Hollow Square pattern
    
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("----------------------------------------------------")

#pascals pattern
n=6
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    c=1
    for j in range(i+1):
        print(c, end=" ")
        c= c*(i-j)//(j+1)
    print()
