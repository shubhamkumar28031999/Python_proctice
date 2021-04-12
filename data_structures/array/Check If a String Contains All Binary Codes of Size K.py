from itertools import product
class Solution:
    def hasAllCodes(self,s,k):
        if (k ** 2) + 1 < len(s):
            helping_array = []
            helping_array.extend(product(['0', '1'], repeat=k))
            for i in range(len(helping_array)):
                helping_array[i] = "".join(helping_array[i])
                if helping_array[i] not in s:
                    return False
            return True
        else:
            return False


        # for i in range(2 ** k):
        #     bin_value = bin(i)[2:] if len(bin(i)[2:]) == k else '0' * (k - len(bin(i)[2:])) + bin(i)[2]
        #     print(bin_value)
        #     if bin_value not in s:
        #         return False
        # return True




if __name__=="__main__":
    s="000110111111101000010101110000111011110110100100111100111101001010101100001010010001100110010000000011101100100000000001001011110111101100001000011010101010001000101011111010110111011001011011110100001110011100010001100111100110010011010010000110111011010000110011100100011010110101111010110000100010001110000101010011000111010001101111110011110001100101101000010001011110100000011101011001100101000010010110001100001110000011001011110110011111110010110101101101001010111010010110111000010011000101010110101011110011100100010110000010001000010010001010111000101011001110010001000110111111000101011000101100100101111001110001001100011100111111000101110110111111010001010000100000110100010010101100100110011101001110010110100000000000110011011011100101111100100010010110011011101100111010001111011001010000011010110011011010000"

    k=19
    print(Solution().hasAllCodes(s,k))