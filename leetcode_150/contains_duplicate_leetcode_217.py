
''' Approach 1: BRUTE FORCE SOLUTION
Time complexity: O(n2) where n is size of the input array
Space complexity: O(1)

'''


# nums = [1,5,3,3,2]

# def contains_duplicate(nums):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
            
#     return False

# print(contains_duplicate(nums))

''' Approach 2: USE SORTING
Sort and then traverse along adjacent elements of the array to find out it they are duplicates
Time complexity: Sorting can take a time complexity of O(nlogn)
Space complexity: O(1)

'''

''' Approach 3: HASHMAP
Sacrifice space complexity to achieve better time complexity  
Time complexity: O(n) (as we only scanned the list of inputs once)
Space complexity: O(n) (could be up to the sice of the input array)

'''

nums = [2,5,3,7,8]
        
def contains_duplicate(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        else:
            hashset.add(num)
    
    return False
    

print(contains_duplicate(nums))




