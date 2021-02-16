def palindrome(s) :  # s : string
    queue = []
    stack = []
    for x in s :
        if x.isalpha() :  # alphabet 인지 확인
            queue.append(x.lower())  # 대소문자 구별 no
            stack.append(x.lower())
    while queue :
        if queue.pop(0) != stack.pop() :
            return False
    return True
print(palindrome('Live evil'))  # True
print(palindrome("Madam, I'm Adam"))  # True
print(palindrome('superman'))  # False


def palindrome2(string):
    i = 0
    j = len(string) - 1
    string = string.lower()
    while j > i :
        if string[i].isalpha() == False:
            i += 1
        elif string[j].isalpha() == False:
            j -= 1
        elif string[i] != string[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

print(palindrome('Live evil'))  # True
print(palindrome("Madam, I'm Adam"))  # True
print(palindrome('superman'))  # False


from collections import deque
qu = deque()
qu.append(1)
qu.append(2)
print(qu.popleft())
print(qu)
print(type(qu))