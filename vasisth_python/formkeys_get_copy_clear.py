d= dict.fromkeys(('name','age','height'),'unknown')
print(d)

c= dict.fromkeys('abc','unknown')
print(c)

b= dict.fromkeys(range(1,11),'unknown')
print(b)

a= dict.fromkeys('abc',['unknown','unknown'])
print(a)


print(d.get('names'))


if d.get('name'):
    print("present")

else:
    print("not present")






