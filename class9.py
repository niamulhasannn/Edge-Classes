#remove specified index
thelist=["apple","banana","cherry"]
thelist.pop(1)
print(thelist)

#

thelist=["apple","banana","cherry"]
thelist.pop()
print(thelist)

#
thelist=["apple","banana","cherry"]
del thelist[0]
print(thelist)

#
'''thelist=["apple","banana","cherry"]
del thelist
print(thelist)'''

#
thelist=["apple","banana","cherry"]
for x in thelist:
    print(x)

#
thelist=["apple","banana","cherry"]
for i in range(len(thelist)):
    print(thelist[1])

# 
thelist=["apple","banana","cherry"]
i=0
while i<len(thelist):
    print(thelist[i])
    i=i+1

#
thelist=["apple","banana","cherry"]
[print(x) for x in thelist]


fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

newlist=[x.upper()for x in fruits]
print(newlist)
newlist=[x if x != "banana" else "orange" for x in fruits]
print(newlist)