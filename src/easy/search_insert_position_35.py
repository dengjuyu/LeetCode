def search_insert(nums, target):
    min_value = nums[0]
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            return -1
