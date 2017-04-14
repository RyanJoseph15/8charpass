# import itertools
import copy

file = open('8charpass.txt', 'w')

# charOptions = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
# charOptions='qQwWeErRtTuUaAzZxXcCvVbBnNmM123456!@#$%^'
charOptions = '123'

charOptionsLength = len(charOptions)
repeatThreshold = 0
length = 4
# charMapTemplate = {}
# for char in charOptions:
#     charMapTemplate[char] = 0
# passes = itertools.permutations(charOptions, length)
# # print(str(len(passes)))
# count = 0

# for pw in passes:
#     permu = {}
#     for char in pw:
#         permu[char] = char
#     # print permu
#     permuStr = ''
#     for char in permu:
#         permuStr += char
#     # print permuStr
#     count += 1
#     if (len(permuStr) == length):
#         permuStr += '\n'
#         file.write(str(permuStr))
#         if (count % 1000000 == 0):
#             # print(str(count) + " permutations")
#             print(str(count/3100796899200))

# charMap = copy.copy(charMapTemplate)
# def append(string, charMap, times):
#     for char in charOptions:
#         if (charMap[char] <= repeatThreshold):
#             newString = string + char
#             if (times == length):
#                 file.write(newString + '\n')
#             if (times < length):
#                 charMap[char] += 1
#                 append(newString, charMap, times + 1)
#     charMap = copy.copy(charMapTemplate)

# append('', charMap, 1)
charSet = {}
for char in charOptions:
    charSet[char] = char
map = {}
def inception(depth, innerMap):
    if (depth < length):
        for char in charOptions:
            if (char == '1'):
                stop = 'here'
            innerMap[char] = inception(depth + 1, copy.deepcopy(charSet))
    else:
        return charSet

inception(0, map)
fin = 'fin'