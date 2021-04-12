from itertools import combinations

def powerset(s):
    l=len(s)
    arr=[]
    for i in range(2**l):
        arr.append([s[j] for j in range(l) if (i & (2**j))])
    return arr
def powerset2(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def powerset3(lst):
    elements=[]
    for i in range(len(lst)+1):
        elements.append(list(combinations(lst,i)))
    print(elements)


def gensets(val, cur_list):
    extension = []
    for cur_set in cur_list:
        tmp = cur_set.copy()
        tmp.append(val)
        extension.append(tmp)
    return extension
def subsets( nums):
    result = [[]]
    for val in nums:
        result.extend(gensets(val, result))
    return result

arr=[1,2,3,4]

print(subsets(arr))