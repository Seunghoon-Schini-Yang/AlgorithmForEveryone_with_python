## Search & Sort

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

# Selection Sort # Ascending Order
# O(n**2)
def Sel_Sort(li):
    n = len(li)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if li[min_idx]>li[j]:  # < : Descending Order
                min_idx = j
        li[i],li[min_idx] = li[min_idx],li[i]
Sel_Sort(list1)
print(list1)

# Insertion Sort # Ascending Order
# O(n**2)
# In case 'li' already sorted : O(n)
def Isrt_Sort(li):
    n=len(li)
    for i in range(1,n) :
        key = li[i]
        j = i-1
        while j>=0 and key<li[j] :  # key>li[j] : Descending Order
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key
Isrt_Sort(list1)
print(list1)


# Merge_Sort # Ascending Order
# O(n*logn)
def Mrg_Sort(li):
    n = len(li)
    if n <= 1:
        return  # None

    mid = n // 2
    li1, li2 = li[:mid], li[mid:]
    Mrg_Sort(li1)  # sort li1
    Mrg_Sort(li2)  # sort li2

    i1 = 0
    i2 = 0
    ili = 0

    while i1 < len(li1) and i2 < len(li2):
        if li1[i1] < li2[i2]:   # > : Descending Order
            li[ili] = li1[i1]   # set value into 'li' in order
            i1 += 1
            ili += 1
        else:
            li[ili] = li2[i2]
            i2 += 1
            ili += 1

    while i1 < len(li1):   # check remains
        li[ili] = li1[i1]   # set remains into li
        i1 += 1
        ili += 1
    while i2 < len(li2):
        li[ili] = li2[i2]
        i2 += 1
        ili +=


# Quick Sort


