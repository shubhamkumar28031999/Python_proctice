#index():- return index of any perticular substring
str="Hello World Hello World"
pos=str.index("World")
print("First Position of word is ",pos)
print("Secod Position of World is = ",str.index("World",pos+1))
input()