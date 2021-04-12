
def swap_case(s):
    str1=list(s)
    for i in range(0,len(str1)):
        if str1[i]==str1[i].upper():
            str1[i]=str1[i].lower()
        else:
            str1[i]=str1[i].upper()

    return "".join(str1)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
