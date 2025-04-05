def search_insert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

def search_insert_binary_version(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    print(search_insert(nums, target))
    print(search_insert_binary_version(nums, target))
