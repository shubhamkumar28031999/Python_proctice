class Solution:
    def printVertically(self, s):
        s=s.split(" ")
        max_len=0
        for word in s:
            max_len=max(max_len,len(word))
        result=[]
        i=0
        for _ in range(max_len):
            temp_word=''
            for val in s:
                if len(val)<i+1:
                    temp_word+=' '
                else:
                    temp_word+=val[i]
            i+=1
            result.append(temp_word.rstrip())
            print(result)
        return result


if __name__=="__main__":
    s=Solution()
    string="TO BE OR NOT TO BE"
    s.printVertically(string)