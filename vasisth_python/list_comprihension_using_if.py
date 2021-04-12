l=list(range(1,11))
print(l)
even_num=list(i for i in l if(i%2==0) )
print(even_num)

new_list=[i*2 if(i%2==0) else -i for i in range(1,20)]
print(new_list)

nested_lc=[[i for i in range(1,4)] for j in range(1,4)]
print(nested_lc)