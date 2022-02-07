class NumArray:

    def __init__(self, nums: List[int]):
        

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left,right+1):
            sum+= nums[i]
        return sum

        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
