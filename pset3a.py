
#### SOLUTION TO MIT-OCW PROBLEM SET 3, Problem 1 ####

def countSubStringMatch(target, key):
    count = 0
    if key is '': return 0
    
    while target:
        r = target.find(key)
        if r == -1: return count
        count += 1;
        target = target[r + len(key):]
    
    return count   


def countSubStringMatchRecursive(target, key):
    if key is '': return 0
    r = target.find(key)

    if r == -1: return 0
    else: 
        return 1 + search_recur (target[r + len(key):], key)

