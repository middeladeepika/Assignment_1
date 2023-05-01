#In general without using any function calls
a=20
b=10
c=a
a=b
b=c
print(a)
print(b)
#print(c) , here output of print(c) is also same as output of print(b) i.e c is also 20 (c=20).

#using function with arguments 
def swap(a,b):
    c=a
    a=b
    b=c
    print(a)
    print(b)
swap(20,10)

#using function without arguments but giving input fixed values inside the function.
def swap():
    a=20
    b=10
    c=a
    a=b
    b=c
    print(a)
    print(b)
swap()

#using function without arguments and by giving different input values in inside the function.
def swap():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    c=a
    a=b
    b=c
    print(a)
    print(b)
swap()



