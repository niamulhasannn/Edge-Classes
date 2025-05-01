'''PYTHON SETS'''
#A set is a collection which is unordered, unchangeable*, and unindexed.
thisset={'apple','banana','cherry'}
print('thisset=',thisset,'\n')
#Duplicates Not Allowed,ignored
demset={'apple','banana','cherry','apple'}
print("demset=",demset,'\n')

'''True and 1 is considered the same value.Similarly
False abnd 0 is considered same'''

set_x={"apple", "banana",1, "cherry", False, True, 0}
print(set_x,'\n')
print(len(set_x),'\n') #prints it's length

print(type(set),'\n',type(list),'\n',type(tuple),'\n',type(dict),'\n')

#sets can take on any datatype, int string boolean

