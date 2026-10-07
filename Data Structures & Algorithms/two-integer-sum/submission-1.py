class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        prevHash = {} #val: index

        for i, n in enumerate(nums): #i - index, n - int
            diff = target - n
            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash[n] = i
                
                

        
        
       


    
                
             