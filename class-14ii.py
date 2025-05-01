'''UPDATE TUPLES'''
#Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#ADD ITEMS
a_tuple = ("apple", "banana", "cherry")
y = list(a_tuple)
y.append("orange")
a_tuple = tuple(y)
print(a_tuple,'\n')
#REMOVE ITEMS
r_tuple = ("apple", "banana", "cherry")
y = list(r_tuple)
y.remove("apple")
r_tuple = tuple(y)
print(r_tuple,'\n')
#Delete
deltuple = ("apple", "banana", "cherry")
'''del deltuple
print(deltuple)''' #this will raise an error because the tuple no longer exists

'''UNPACK TUPLES'''
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
''''variable less than values?use * to store multiple items in a
single variable as a list'''
vfruits=("apple", "banana", "cherry", "strawberry", "raspberry")
(m,n,*P)=vfruits
print('\n m=',m,'\n n=',n,'\n P=',P,'\n')

(G,*T,R)=vfruits
print('\n G=',G,'\n T=',T,'\n R=',R,'\n')
#loop through items
for x in fruits:
    print(x)
#loop through index
for i in range(len(fruits)):
    print(fruits[i])
#WHILE LOOP
while i<len(fruits):
    print(fruits[i],'\n')
    i=i+1

#can join tuples using + operator
#multiply tuple
myTuple=fruits*2 #copy of item
print(myTuple,'\n')
