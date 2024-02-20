'''
Check if 2 strings are rotation of one another
ex. - abcde, eabcd and by how many places it has been rotated
'''

# s1 = "abcde"
# # s2 = "eabcd"
# s2 = "eabcc"
# first_character = s1[0]
#
# output = len(s1) - s2.index(first_character)
# print(output)

s1 = "abcde"
# s2 = "dabcd"
s2 = "eabcd"

index = 0
# for i in range(len(s1)-1):  # s2
#     # print(f"Value of i : {i}")
#     # print(f"s1[i] :{s1[i]}")
#     # print(f"s2[i] :{s2[i]}")
#     print(f"Value of i : {i}")
i =0
for j in range(len(s2)-1):
    print(f"s1[i] :{s1[i]}")
    print(f"s2[j] :{s2[j]}")
    if s1[i] == s2[j]:
        print(f"Matching : {s1[i]}")
        index = j
        print(f"!! Index : {index}")
        break
    else:
        print("Not matching")

print(f"Index : {index} ")
print("\n Output")
print(s2[index:])
print(s1[len(s1)-index])

if s2[index:] == s1[:len(s1)-index] and s2[:index] == s1[len(s1)-index:]:    # 2nd condition added
    print(f"Rotating by {index} rotation clockwise")
else:
    print("Not rotating")
