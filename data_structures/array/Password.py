for _ in range(int(input())):
    s=input()
    l=len(s)
    if l>=10:
        capital_letter=False
        small_letter=False
        number=False
        special_car=[ '@', '#', '%', '&', '?']
        char=False
        for i in range(l):
            if s[i].islower():
                small_letter=True
            elif s[i].isupper() and i>0 and i<l-1:
                capital_letter=True
            elif s[i].isnumeric() and i>0 and i<l-1:
                # print(s[i])
                number=True
            elif ( s[i]=='@'or s[i]=='#'or s[i]=='%'or s[i]=='&'or s[i]=='?') and i>0 and i<l-1:
                char=True
        if capital_letter and small_letter and number and char:
            print('YES')
        else:
            print('NO')

    else:
        print('NO')