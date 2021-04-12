def checkPangram(str):
    all_words={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    string=set()
    length=len(str)
    for i in range(length):
        if (str[i]<= "Z" and str[i]>="A") or (str[i]<= "z" and str[i]>="a"):
            string.add(str[i].lower())
        else:
            pass
    set1 = all_words.intersection(string)
    if(set1==all_words):
       print(1)
    else:
        print(0)

num=int(input(""))
for i in range(num):
    str=input("")
    checkPangram(str)