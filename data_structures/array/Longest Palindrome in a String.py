if __name__ == "__main__":
    for _ in range(int(input())):
        st = input()
        l = len(st)
        max_len = 1
        max_str = st[0]
        for i in range(l):
            for j in range(i+1,l+1):
                if st[i:j] in st[i:j][::-1]:
                    if max_len < (j - i + 1):
                        # print(st[i:j])
                        max_len = j - i + 1
                        max_str = st[i:j]
        print(max_str)
# otafsngqvoijxuvqbztv
# aaaabbaa