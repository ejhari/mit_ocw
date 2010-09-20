
#### SOLUTION TO MIT-OCW PROBLEM SET 3, Problem 2 ####

from string import find

def subStringMatchExact(target, key):
    result, location, index = [], 0, 0
    
    if target == '' or key == '': return result
    while target:
        location = find(target, key, index)
        if location == -1: return result
        else: 
            result.append(location)
            index = location + len(key)
    
    return result


