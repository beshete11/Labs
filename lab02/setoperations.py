def make_set(data):
    new_list = []
    for num in data:
        if num not in new_list:
            new_list.append(num)
    print(new_list)

def is_set(data):
    checked = {}
    for num in data:
        if num in checked:
            return False
        checked[num] = True
    return True



def union(set1, set2):
    if is_set(set1) == False or is_set(set2) == False:
        return []
    if is_set(set1) == True and is_set(set2) == True:
        new_set = []
        for num in set1 + set2:
            if num not in new_set:
                new_set.append(num)
        print(new_set)


def intersection(set1, set2):
    if is_set(set1) == False or is_set(set2) == False:
        return []
    if is_set(set1) == True and is_set(set2) == True:
        inter_set = []
        for num in set1 + set2:
            if num not in inter_set:
                inter_set.append(num)
        print(inter_set)


intersection([1,2],[2,3])
