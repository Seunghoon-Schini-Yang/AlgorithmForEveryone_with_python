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