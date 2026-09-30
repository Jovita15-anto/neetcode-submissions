class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap ={}

        for i ,num in enumerate(nums):
            dif = target - num
            if dif in prevmap:
                return [prevmap[dif], i] 
            prevmap[num] = i
        return       
        