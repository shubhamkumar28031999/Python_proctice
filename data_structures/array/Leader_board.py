import sys
def Solve(n,leader_current,m,score_arr):
    leader_current=sorted(list(set(leader_current)),reverse=True)
    i=len(leader_current)
    print(leader_current)
    j=0
    arr=[]
    while i>=0:
        print(f"i_top={i}")
        if j<m and leader_current[i-1]>score_arr[j]:
            arr.append(i+1)
            print(f"i_inside_if={i}")
            j+=1
        elif i==0 and leader_current[i-1]<score_arr[j]:
            arr.append(i+1)
            j+=1
            i-=1
        else:
            i-=1
    print(arr)

if __name__=="__main__":
    n=7
    leader_current=[100,100,50,40,40,20,10]
    m = 4
    score_arr = [5,25,50,105]
    Solve(n,leader_current,m,score_arr)