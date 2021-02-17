list1 = [6, 3, 7, 4, 6, 6, 8, 2, 5]


# Selection Sort # Ascending Order
# O(n**2)
def Sel_Sort(li):
    n = len(li)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if li[min_idx] > li[j]:  # < : Descending Order
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]


Sel_Sort(list1)
print(list1)


# Insertion Sort # Ascending Order
# O(n**2)
# In case 'li' already sorted : O(n)
def Isrt_Sort(li):
    n = len(li)
    for i in range(1, n):
        key = li[i]
        j = i-1
        while j >= 0 and key < li[j]:  # key>li[j] : Descending Order
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
        ili += 1


# Quick Sort
def Qck_Sort_1(li):
    n = len(li)
    if n <= 1:
        return li

    pivot = []
    smaller = []
    bigger = []
    key = li[-1]

    for i in li:
        if i > key:
            bigger.append(i)
        elif i < key:
            smaller.append(i)
        else:
            pivot.append(i)
    return Qck_Sort_1(smaller) + pivot + Qck_Sort_1(bigger)


print(Qck_Sort_1([7, 3, 8, 1]))


def Qck_Sort_2(li):
    n = len(li)
    if n <= 1:
        return

    key = li[-1]
    i = 0
    for j in range(0, n-1):
        if li[j] < key:
            li[i], li[j] = li[j], li[i]
            i += 1

    li[i], li[-1] = key, li[i]

    li1 = li[:i]
    li2 = li[i+1:]

    Qck_Sort_2(li1)
    Qck_Sort_2(li2)

    li[:i] = li1
    li[i+1:] = li2


li_ex = [9, 6, 7, 3, 8, 1]
Qck_Sort_2(li_ex)
print(li_ex)


# Bubble Sort
# O(n^2)
def Bubl_Sort(li):
    n = len(li)
    i = 1
    while i == 1:
        i = 0
        for j in range(n-1):
            if li[j+1] < li[j]:
                li[j+1], li[j] = li[j], li[j+1]
                i = 1


Bubl_Sort(list1)
print(list1)
