#1
fruits=["apple","banana","kiwi","cherry","mango"]
newlist=[ x for x in fruits if x != "apple"]
print(newlist)
#2
fruits=["apple","banana","kiwi","cherry","mango"]
newlist=[x if x != "banana" else "orange" for x in fruits]
print(newlist)
#3
fruitlist=["grape","Apple","orange","Banana"]
fruitlist.sort(key=str.lower)
print(fruitlist)

#4
tools=["pen","book","eraser","pencil"]
tools.reverse()
print(tools)

#5
#i
thislist=["pen","book","eraser","pencil","grape","Apple","orange","Banana"]
newlist=thislist.copy()
print(newlist)
#ii
thislist=["pen","book","eraser","pencil","grape","Apple","orange","Banana"]
newlist=list(thislist)
print(newlist)
#iii
thislist=["open","book","eraser","pencil","grape","Apple","orange","Banana"]
newlist=thislist[:]
print(newlist)



#NEWCLASS

#A tuple is a collection which is ordered and unchangeable 
#Allow duplicate 
thistuple=("apple","banana","cherry")
print(thistuple)

#length 
thistuple=("apple","banana","cherry")
print(len(thistuple))

#one item tuple, remember the comma

thistuple=("apple",)
print(type(thistuple))

#note a tuple
thistuple=("apple")
print(type(tuple))

#tuple items can be of any data type 
tuple1=("apple","banana","cherry")
tuple2=(1,5,7,9,3)
tuple3=(True,False,False)

mytuple=("apple","banana","cherry")
print(type(mytuple))

thistuple=tuple(("apple","banana","cherry"))
print(thistuple)

thistuple=("apple","banana","cherry")
print(thistuple[1])

thistuple=("apple","banana","cherry")
print(thistuple[-1])

thistuple=("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])

thistuple=("apple","banana","cherry")
if "apple" in thistuple:
    print("yes, 'apple'is in the fruits tuple")

#convert the tuple into a list to be able change it 
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)

print(x)