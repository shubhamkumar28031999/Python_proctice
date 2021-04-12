def reverse(string):
    stack=[]
    for i in string[::-1]:
        stack.append(i)
    string="".join(stack)
    return string

print(reverse("aksd"))