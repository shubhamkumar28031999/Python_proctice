class Solution:
    def isOneBitCharacter(self, bits):
        l=len(bits)
        n=0
        while n<l:
            if n<l-2:
                if bits[n:n+2]==[1,0] or bits[n:n+2]==[1,1]:
                    n+=2
                else:
                    n+=1
            else:
                if bits[n:l]==[1,0] or bits[n:l]==[1,1]:
                    return False
                else:
                    return True



if __name__=="__main__":
    bits = [1, 0, 0]
    print(Solution().isOneBitCharacter(bits))