#check the string is either present
txt="The best things in life are freee!"
print("free" in txt)

if "free"in txt:    
    print("Yes,'free' is present.")

print( "expensive" not in txt)
if"expensive" not in txt:
    print("No,'expensive' is not present.")

#slicing
b=" Hello, world! "
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])
#make a sentence fully upercase or lowercase
print(b.upper())
print(b.lower())
#remove white space from beginning and end
print(b.strip())
#replace letter
print(b.replace("H","J"))
#split into two part
print(b.split(","))

age = "36"
newtxt = "My name is John, I am " + age
print(newtxt)

age = 36
newtxt = f"My name is John, I am {age}" 
print(newtxt)

