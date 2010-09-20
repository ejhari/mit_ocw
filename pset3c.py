
#### SOLUTION TO MIT-OCW PROBLEM SET 3, Problem 3 ####

def constrainedMatchPair(firstMatch, secondMatch, length):
    result = []
    
    for i in firstMatch:
        for j in secondMatch:
            if i + length + 1 == j:
                secondMatch.remove(j)
                result.append(i)
    
    return result
    

def generate(target, key):
    output = subStringMatchExact(target, key)
    key1, key2 = '', key[1:]
    
    while key2:
        starts1 = subStringMatchExact(target, key1)   
        starts2 = subStringMatchExact(target, key2)
    
        output.extend(constrainedMatchPair(starts1, starts2, len(key1)))
        
        key1, key2, key = key1 + key[0], key2[1:], key[1:]
        
    return sorted(list(set(output)))

 
