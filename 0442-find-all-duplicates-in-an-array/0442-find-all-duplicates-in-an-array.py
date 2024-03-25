class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c=[]
        for i in nums:
            i=abs(i)   
            if nums[i-1]<0:
                c.append(i)
            nums[i-1]=-nums[i-1]
        return c
        
        