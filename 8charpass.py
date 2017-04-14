# import itertools
import copy

file = open('8charpass.txt', 'w')

# charOptions = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
charOptions='qQwWeErRtTuUaAzZxXcCvVbBnNmM123456!@#$%^'
# charOptions = '123456'

charOptionsLength = len(charOptions)
repeatThreshold = 0
length = 3

def append(string, times):
    for char in charOptions:
        charCount = string.count(char)
        if (charCount <= repeatThreshold):
            newString = string + char
            if (times == length):
                file.write(newString + '\n')
            if (times < length):
                append(newString, times + 1)

append('', 1)