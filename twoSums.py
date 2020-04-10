def twoSum(nums, target):
    sums = {}
    for i, j in enumerate(nums):
        difference = target - j
        sums[j] = i
        
        if difference in sums:
            print([sums[difference], i])
            break
        
        if i == (len(nums) - 1):
            print("No solution.")
# TEST CASES
twoSum([2, 7, 12, 15], 9)
twoSum([12, 15, 2, 7, ], 9)
twoSum([2, 12, 15], 9)
twoSum([0, 2, 12, 15], 15)
twoSum([], 9)
