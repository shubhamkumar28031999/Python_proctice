def from_left(p):
    turn=0
    temp_page_no=1
    while temp_page_no<p:
        temp_page_no+=2
        turn+=1
    return turn

def from_right(n,p):
    if n%2==0:
        n=n
    else:
        n= n-1
    turn=0
    while n>p:
        turn+=1
        n-=2
    return turn

def pageCount(n, p):
    return min(from_right(n,p),from_left(p))

if __name__=="__main__":
    print(pageCount(6,2))