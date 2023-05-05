''' 1Q: Alice was bored that day,so she was sitting on the riverbank.suddenly she notices a talking ,white Rabbit with a pocket watch.it ran fast,and she followed it,down a rabbit hole.she fell
into the hole and found a magical wonderland with dark trees,beautiful flowers.she found many ways numbered from 1,2,3.........18.she was confused which is the right way that will lead her
to her home.she found a cute bird,standing in one of the trees.Alice asked the bird the way to go back to her home.The bird said a two-digit number(say 23) and asked her to find the sum of
its digits(2+3=5) and that numbered way will lead her to her home.Alice was already confused ,so pls help Alice in finding the route to her home...

Input format:

input consists of an integer corresponding to the 2-digit number.

output format

the output consists of an integer corresponding to the sum of its digits.


Refer sample input and output for formating speciations.[All text in bold corresponds to input and the rest corresponds to output]

SAMPLE INPUT -OUTPUT:

23

OUTPUT

5'''
#By seeing question General analysing data without using any function calls..
#a = int(input("enter any 1-digit number"))
#b = int(input("enter any 1-digit number"))
#n = a+b
#if n<=18:
 #print("a,b,n is :",a,b,n)
#else:
   # print("no way")

#By using if condtion.
n = int(input(' '))
if n<=99:
    a = n//10
    b = n%10
    s = a+b
print(s)

#By using function with arguments.
def way(n):
    if n<=99:
        a = n//10
        b = n%10
        s = a+b
    if s<=18:
        print(s)
way(23)
    
