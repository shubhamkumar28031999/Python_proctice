def palindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        string=input()
        check_palindrome=palindrome(string)
        if check_palindrome:
            print(-1)
        else:
            string=sorted(string)
            l="".join(string)
            print(l)


