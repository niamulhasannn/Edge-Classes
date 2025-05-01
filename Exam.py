#1

fruits=["apple","banana","kiwi","cherry","mango"]
fruits.pop(2)
print(fruits)

#2

fruits=["apple","banana","kiwi","banana","mango"]
fruits.remove("banana")
print(fruits)

#3
colors=["red","green","blue","yellow"]
for x in colors:
    print(x)


#4
names=["Alice","Bob","Charlie","Diana"]
i=0
while i<len(names):
    print(names[i])
    i=i+1

#5

fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "e" in x]
print(newlist)
