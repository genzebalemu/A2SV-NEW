class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count =0
        list=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[j]<nums[i]:
                    count+=1
            list[i]=count
            count=0
        
        
        return list