def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

#string = input("Enter your String:")
#stringToReturn = string_both_ends(string)
#print(stringToReturn)

def divis_7(int1, int2):
    for i in range(int1, int2):
        if (i % 7 == 0) & (i % 5 != 0):
            print(i)
print("Intput first num range")
num1 = int(input())
print("Input second num range:")
num2 = int(input())
print(divis_7(num1, num2))