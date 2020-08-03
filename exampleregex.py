import re

nameRegex = re.compile(r'Agent \w+')
# regex matches Agent space first word
# print(nameRegex.findall('Agent Rob will meet Agent Ann today ?'))

# .sub() => Replace=> Agent Name replaced with CLASS
# print(nameRegex.sub('CLASS', 'Agent Rob will meet Agent Ann today ?'))

# To get only the starting Letter of matching name
nameRegex = re.compile(r'Agent (\w)\w*')
# print(nameRegex.findall('Agent Rob will meet Agent Ann today ?'))

# To replace the Name with * except the starting Letter
print(nameRegex.sub(r'Agent \1***', 'Agent Rob will meet Agent Ann today ?'))

# searchstr = 'helloo##oo5^'
# pattern = re.compile(r"[a-zA-Z0-9%$#@]{8,}\d")
#
# a = pattern.fullmatch(searchstr)
# print(a)
