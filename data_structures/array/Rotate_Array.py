# def reverse(arr, opr):
#     temp_arr = arr[:opr[1]]
#     for i in range(opr[0] - opr[1]):
#         arr[i] = arr[i + opr[1]]
#     arr[opr[0] - opr[1]:] = temp_arr
#
#     for j in range(opr[0]):
#         print(arr[j], end=" ")
#
# test_case = int(input(""))
# operations = []
# lists = []
# for i in range(test_case):
#     operation = list(map(int, input().split()))
#     list_list = list(map(int, input().split()))
#     operations.append(operation[:2])
#     lists.append(list_list[:operation[0]])
#
# for i in range(test_case):
#     reverse(lists[i], operations[i])
#

def reverse(arr, opr):
    temp_arr = arr[:opr[1]]
    for i in range(opr[0] - opr[1]):
        arr[i] = arr[i + opr[1]]
    arr[opr[0] - opr[1]:] = temp_arr

    for j in range(opr[0]):
        print(arr[j], end=" ")
    print("\n")

test_case = int(input(""))
operations = []
lists = []
for i in range(test_case):
    operation = list(map(int, input().split()))
    list_list = list(map(int, input().split()))
    operations.append(operation[:2])
    lists.append(list_list[:operation[0]])
    reverse(lists[i], operations[i])

