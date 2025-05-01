#newlist= [expression for item in iterable if condition=True]
fruits=["apple","banana","kiwi","cherry","mango"]
newlist=[ x for x in fruits if x != "apple"]
newlist2=[x for x in range(10)]
newlist3=[x if x != "banana" else "orange" for x in fruits]

print(newlist)
print(newlist2)
print(newlist3)


#sort list aplhanumerically

thislist=["orange","mango","kiwi","Pinapple","banana"]
thislist.sort()
print(thislist)

thislist=[100,50,68,82,23]
thislist.sort()
print(thislist)

#sort decending
thislist=["orange","mango","kiwi","Pinapple","banana"]
thislist.sort(reverse=True)
print(thislist)

#customize sort function 
def myfunc(n):
    return abs(n-50)
thislist=[100,50,68,82,23] 
thislist.sort(key=myfunc) #key = function argument 
print(thislist)

#case insensitive sort of the lsit
thislist=["banana","Orange","Kiwi","cherry"]
thislist.sort(key=str.lower)
print(thislist)

#reverse the list
thislist=["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)

#use the copy() method
thislist=["banana","Orange","Kiwi","cherry"]
mylist= thislist.copy()
print(mylist)

#use the list() method

thislist=["apple","banana","cherry"] #make a copy of a list with the list()
mylist=list(thislist)
print(mylist)

#use the slice operator 
thislist=["apple","banana","cherry"]
mylist=thislist[:]
print(mylist)

#join two lists 
list1=["a","b","c"]
list2=[1,2,3]

list3=list1+list2
print(list3)

#append list2 into list1

