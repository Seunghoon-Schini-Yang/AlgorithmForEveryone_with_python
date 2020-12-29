## Search & Sort

# Sequential Search
def seqsear(li,val):
    for i in range(len(li)):
        if val==li[i]:
            return i  # return index
    return -1  # no val in list
print(seqsear([9,2,2,3],4))
print(seqsear([9,2,2,3],2))  # return index of fisrt val

def seqsear2(li,val):
    ans = []
    for i in range(len(li)):
        if val==li[i]:
            ans.append(i)  # return all index of val
    return ans
print(seqsear2([9,2,2,3],2))

# Selection Sort
