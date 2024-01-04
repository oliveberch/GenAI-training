# list access
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0])
# Index starting from 0

# list slice

print(thislist[2:5])

#Insert "watermelon" as the third item:
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)

# Extend list

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove list items

thislist.clear()
print(thislist)


subs = ["eng", "maths", "science"]
marks = []
i = 0

for sub in subs:
    for mark in marks:
    marks.append(int(input("Enter marks for",sub)))


#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple[1] = "cherry"
