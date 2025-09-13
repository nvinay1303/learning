'''
Approach 1: Hashmap

Time complexity: O(s+t) = O(n)
Space complexity: O(n)
'''
s = 'campm'
t = 'acppm'

def valid_anagram(s, t):
    if len(s)!=len(t):
        return False
    
    countS, countT = {}, {}    
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)

    # for j in s:
    #     if j not in countT.keys():
    #         return False
    #     elif countS[j] != countT[j]:
    #         return False
        
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
        
    return True

print(valid_anagram(s, t))

'''
Approach 2: Counter data structure

solution - Counter(s) == Counter(t)
'''

'''
Approach 3: Sorting
Bubble sort - n2
Good algos - nlogn

solution - sorted(s) == sorted(t) 
'''

    



