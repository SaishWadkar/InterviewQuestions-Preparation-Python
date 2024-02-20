'''
aaaaabbbccdaa -> a5b3c2d1a2
'''

# def compress_string(s):
#     compressed_string = ""
#     count = 1
#
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed_string += s[i - 1] + str(count)
#             count = 1
#
#     compressed_string += s[-1] + str(count)
#
#     return compressed_string
#
# input_string = "aaaaabbbccdaa"
# result = compress_string(input_string)
# print(result)

s = "aaaaabbbcc"
count = 1
result = ""

for i in range(len(s)-1):
    print(f"{s[i]} and {s[i+1]}")
    if s[i]==s[i+1]:
        count+=1
    else:
        result = result + s[i] + str(count)
        count = 1

    print(f"Count : {count}")

result = result + s[-1] + str(count)
print(f"Result : {result}")


# s_list = list(s)
# print(s_list)
#
# s_string = ",".join(s_list)
# print(s_string)

# import re
#
# input_string = "aaaaabbbccdaa"
# pattern = r'([a-zA-Z])(\1*)'
#
# result = re.findall(pattern, input_string)
# split_string = ''.join([group[0] + str(len(group)) for group in result])
#
# print(split_string)
