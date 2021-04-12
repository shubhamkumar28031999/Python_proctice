string= input("enter any string to check weather it's a palindrome or not")

print(''.join(reversed(string)))
if  string[::-1]==string:
    print("its a palindrome")
else:
    print("it's not a palindrome")