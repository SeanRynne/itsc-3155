
#part 1

def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

string = input("Enter your String:")
stringToReturn = string_both_ends(string)
print(stringToReturn)

#part 2

def divis_7(int1, int2):
    for i in range(int1, int2):
        if (i % 7 == 0) & (i % 5 != 0):
            print(i)
print("Intput first num range")
num1 = int(input())
print("Input second num range:")
num2 = int(input())
print(divis_7(num1, num2))

#part 3

def dictCombine(a, d):
    for i in d:
        if i in a:
            d[i] = d[i] + a[i]
    hold = {**a, **d}
    print(hold)

people = {'a': 100, 'b': 200, 'c': 300}
friends = {'a': 300, 'b': 200, 'd': 400}
dictCombine(people, friends)

#part 4

print("Number of items: ")
numItems = int(input())
holdEnd = numItems

itemList = dict()
for i in range (numItems):
    holder = input(("Input item and price: "))
    temp = holder.split(" ")
    itemList[temp[0]]=int(temp[1]) 
    #this sets the split where into the dictionary 
    #with the first word being the key, second num being the value
    sortList = sorted(itemList.items(), key = lambda item:item[1])
    #quick google search to find how to sort a dictionary from value
#print(sort)
x = 0
while x < holdEnd:
    print(sortList[x])
    x = x + 1