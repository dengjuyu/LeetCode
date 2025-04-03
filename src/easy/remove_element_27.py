class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# 테스트 코드
if __name__ == "__main__":
    solution = Solution()

    # 테스트 케이스
    nums = [3, 2, 2, 3]
    val = 3
    result = solution.removeElement(nums, val)

    # 결과 출력
    print(f"After removing {val}, the length is: {result}")
    print(f"Updated list: {nums[:result]}")