class Solution:
    def maxProfit(self, prices, fee):
        obsp=float('-inf')
        ossp=0
        for i in range(len(prices)):
            nbsp,nssp=obsp,ossp
            obsp=max(nssp-prices[i],nbsp)
            ossp=max(nbsp+prices[i]-fee,nssp)
        return ossp

if __name__=="__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee=2
    print(Solution().maxProfit(prices,fee))