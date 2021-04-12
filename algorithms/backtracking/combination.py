class Solution:
    def powerset(self, s):
        global j
        final_list = []
        x = len(s)
        for i in range(1 << x):
            final_list.append([s[j] for j in range(x) if (i & (1 << j))])
        return final_list

    def combination_sum_without_repetition(self, s, target):
        final_arr = []
        global j
        x = len(s)
        for i in range(1 << x):
            t = [s[j] for j in range(x) if (i & (1 << j))]
            if sum(t) == target:
                final_arr.append(t)
        return final_arr

    def combination_sum_with_repetion(self, s, target):
        print(self.ret_sum(s, target, 0, []))

    def ret_sum(self, candidate, target, index, sublist, lst=[]):
        elements = []
        if target == 0:
            return lst.append(sublist)
        if target < 0:
            return
        else:
            for i in range(index, len(candidate)):
                sublist.append(candidate[i])
                lst.append(self.ret_sum(candidate, target - candidate[i], i, sublist, lst))
                sublist.remove(candidate[i])
                return lst

    # def akad(self,arr,target):
    #     element=[]
    #     l=len(arr)
    #     for i in range(l):
    #         temp=target
    #         for j in range(i,l):
    #             if



if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    # print(powerset(arr))
    print(Solution().combination_sum_with_repetion(arr, 8))
