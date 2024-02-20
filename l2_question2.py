'''
Reverse the vowels in the strings --- umbrella -> ambrellu
u
e
a
'''

s = "umbrella"

vowels = []
for i in s:
    if i in ["a","e","i","o","u"]:
        vowels.append(i)
print(vowels)

# got vowels here

s2 = list(s) # convert original string to list
print(s2)
# result = s2.copy()

# result = s

# print(f"Result : {result}")

counter = len(vowels) - 1
print(f"Counter : {counter}")

# sol 1
# for i in s:
#     if i in ["a", "e", "i", "o", "u"]:
#         print(i)
#         s = s.replace(i,vowels[counter])
#         print(s)
#         counter = counter -1
#         print()
# print(f"Answer : {s} ")


# sol 2
# for i in range(len(s2)-1):
#     # print(f"Value of i : {i}")
#     if s2[i] == "a" or s2[i] == "e" or s2[i] == "i" or s2[i] == "o" or s2[i] == "u":
#         print(f"Value of index : {i}")
#         result.insert(i,vowels[counter])
#         result.remove(s2[i])
#         counter = counter -1
#
#     else:
#         print("In else")


# solution
for i,j in enumerate(s):
    if j in ['a','e','i','o','u']:
        s2.insert(i,vowels[counter])
        s2.pop(i+1)
        counter=counter-1

print(f"Output : {s2}")
op = "".join(s2)
print(op)


#  umbrella -> ambrellu

'''
Binary Search
search =4
mid = 4
first
last
mid =search
[1,2,3,4,5,6,7]
'''