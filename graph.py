## Find all friends

friend_info = {
    'Summer' : ['John','Justin','Mike'],
    'John' : ['Summer','Justin'],
    'Justin' : ['John','Summer','Mike','May'],
    'Mike' : ['Summer','Justin'],
    'May' : ['Justin','Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

def find_all_friends(fr_info, start_name) :
    qu = []
    done = set()
    qu.append(start_name)
    done.add(start_name)
    while qu :
        p = qu.pop(0)
        print(p)
        for i in fr_info[p] :
            if i not in done :
                qu.append(i)
                done.add(i)

find_all_friends(friend_info,'Summer')
print()
find_all_friends(friend_info,'Jerry')


s = {
    1 : [2,3],
    2 : [1,4,5],
    3 : [1,6,7],
    4 : [2],
    5 : [2],
    6 : [3],
    7 : [3]
}

def BFS(dict,start) :
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    while qu :
        p = qu.pop(0)
        print(p)
        for i in dict[p] :
            if i not in done :
                qu.append(i)
                done.add(i)
BFS(s,1)  # 1 - 2 - 3 - 4 - 5 - 6 - 7

def DFS(dict,start) :
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    while qu :
        p = qu.pop()
        print(p)
        for i in dict[p] :
            if i not in done :
                qu.append(i)
                done.add(i)
DFS(s,1)  # 1 - 3 - 7 - 6 - 2 - 5 - 4