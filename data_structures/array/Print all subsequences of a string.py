def combination_sum_without_repetition(s):
    final_arr = []
    global j
    x = len(s)
    for i in range(1 << x):
        t = [s[j] for j in range(x) if (i & (1 << j))]
        if t==[]:
            pass
        else:
            print("".join(t),end=" ")
    return final_arr

if __name__=="__main__":
    s='abc'
    combination_sum_without_repetition(s)