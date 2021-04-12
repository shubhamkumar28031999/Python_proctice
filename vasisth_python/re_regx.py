import re
string="'I AM NOT YELLING', she said. Through we knew it to not be true."
print(string)
new=re.sub('[A-Z]','',string)
print(new)
new=re.sub('[a-z]','',string)
print(new)
new=re.sub('[.,\']','',string)#/to remove extra symbols
print(new)
new=re.sub('[.,\'a-z]','',string)
print(new)
new=re.sub('[.,\'a-z+" "]','',string)#/to remove spaces
print(new)