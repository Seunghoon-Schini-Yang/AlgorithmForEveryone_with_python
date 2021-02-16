list1 = [6,3,7,4,6,6,8,2,5]

# Sequential Search
def Seq_Srch(li,val):
    for i in range(len(li)):
        if val==li[i]:
            return i  # return index
    return -1  # no val in list
print(Seq_Srch(list1,9))
print(Seq_Srch(list1,2))  # return index of fisrt val

def Seq_Srch_2(li,val):
    ans = []
    for i in range(len(li)):
        if val==li[i]:
            ans.append(i)  # return all index of val
    return ans
print(Seq_Srch_2(list1,6))



sorted_list = [1,3,9,22,27,30,31,32,39,41,43,46,51,55]

# Binary Search
# O(logN)
# recursion & try,except
def Binary_Srch_1(li, val) :
    n = len(li)
    idx = 0
    try :
        if n == 1 and li[n // 2] != val :
            idx = '-1'
        elif li[n // 2] == val :
            idx += n // 2
        elif val > li[n // 2] :
            idx += n // 2 + 1 + Binary_Srch(li[n // 2 + 1:], val)
        else :
            idx += Binary_Srch(li[:n // 2], val)
        return idx
    except :
        return '-1'

print(Binary_Srch_1(sorted_list, 51))


def Binary_Srch_2(li, val) :
    end = len(li)
    start = 0
    while end > start :
        mid = (end + start) // 2
        if li[mid] == val :
            return mid
        elif li[mid] > val :
            end = mid
        elif li[mid] < val :
            start = mid + 1
    return -1

print(Binary_Srch_2(sorted_list, 8))