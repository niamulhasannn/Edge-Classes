fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x.upper()for x in fruits]
newlsit=[x if x != "banana" else "orange" for x in fruits]