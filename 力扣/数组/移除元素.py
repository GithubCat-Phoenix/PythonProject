class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for _ in nums:
            if _ == val:
                nums.remove(val)

        return len(nums)

    a = removeElement([0,1,2,2,3,0,4,2], 2)
    print(a)

