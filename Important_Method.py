
#Question 1
LIST=[1,2,3,4,5]
print(list(reversed(LIST)))

#Question 2
str=input("Enter A string")
for i in range(len(str)):
    if str[i].isupper():
        print(str[i])

#Question 3
a=input("Enter").split(",")
list=[]
for i in a:
    list.append(int(i))#typecast into integer
print(list)

#Question 4
n=int(input("Enter-number"))
b=n
rem=0
result=0
while n!=0:
    rem=n%10
    result=result*10+rem
    n//=10
if b==result:
    print("It is aPalandromic Number")
else:
    print("It is Not a Palandromic Number")

#Question 5
from copy import *
print("DeepCopy:- ")
list1 = ['a','b',['ab','ba']]

list2 = deepcopy(lst1)

list2[2][1] = "d"
list2[0] = "c";

print(list2)
print(list1)
print("Shallow Copy:- ")
list3=list1
list3[0]="hi"
print(list3)
print(list1)
#SHALLOW COPY:A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
#DEEP COPY:A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."""

