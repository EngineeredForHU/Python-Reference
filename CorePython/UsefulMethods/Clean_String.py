# Practice
import re

names = ['angel!#','   gigi',' adrian  ']

def clean_punctuation(value):
    return re.sub("[!#$?]","", value)

clean_ops = [str.strip,clean_punctuation,str.title]

print(f"Before cleaning\n{names}")

def clean_string(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

print("\nAfter putting it into clean_string function")
print(clean_string(names,clean_ops))

