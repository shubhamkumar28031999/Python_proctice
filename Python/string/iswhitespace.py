#isspace():- return ture is string contains only white space characters otherwise return false
#\n
#\t
#space
#\v
#\f
#\r
str=" \t\n\v\f\r"
print(str.isspace())
str=" \t\n\v\f\rm"
print(str.isspace())
input()