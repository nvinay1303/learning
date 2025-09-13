

nums = [5,7,11,14]
target = 12

# def two_sum(nums, target):

#     hashmap = {}

#     for i in range(len(nums)):
#         diff = target-nums[i]
#         print("diff=", diff)
#         if diff in hashmap.keys():
#             return [hashmap[diff], i]
#         hashmap[nums[i]]=i
#     return "not found"

# print(two_sum(nums, target))

def two_sum(nums, target):
    hashmap = {}

    for idx, val in enumerate(nums):
        diff = target - val
        if diff in hashmap:
            return (idx, hashmap[diff])
        hashmap[val]=idx
        
    return "not found"
print(two_sum(nums, target))
            