def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count

if __name__ == '__main__':

    s='abbbaacc'
    result = alternatingCharacters(s)

    print(str(result) + '\n')


