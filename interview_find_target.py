








# You are given an array of integers nums and an integer target, return indices of # the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not  use the same element twice.
# You can return the answer in any order.

# Example 1:
#nums = [2,7,11,15]
#target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]



def find_target(nums: list, target: int) -> list:
    index_dict = {}
    index = 0
    answer = []
    for num in nums:
        #print(f"number is: {num}")
        
        #the case is next because we first check if sub already in the dictinary
        #first num from the list will be added - cause dictioanary is empty
        #second num will start to check if sub exist and if it there means sub been added before!!!
        #so if sub was added before and EXIS in the dictionary and sub=target-num means sub + num = target SO index of the current num has the second index which we need to take!!!! BINGO!! we just take the current INDEX and add it
        #so even [3,3] case will be working and we do not think about to add second time key 3 cause first been existing
        #in this solution we do not return from the if and this can return when we have more then one pairs ,example target=5 nums=[1,2,3,4] will return [1,2,0,3] and this is ok
        
        sub = target - num
        
        if sub in index_dict.keys(): #so the case if sub EXIST in the dictionary means current NUM has the index which as well can be added
           
           
           answer.append(index_dict[sub])  
           answer.append(index)      
            
        
        index_dict[num] = index 
        
        index += 1        
            
    print(f"index_dict: {index_dict}")   # index_dict: {2: 0, 7: 1, 11: 2, 15: 3} 
    return answer


#######################the same solution but little bit different way ###########
def find_target_second_option(nums: list, target: int) -> list:
    my_dict = {}
    answer = []
    index = 0
    for index, num in enumerate(nums): #loop over nums with index and nums
        sub = target - num
        
        #in this solution we return when we see first pair and do not wait for next pairs if they exist!!
        if sub in my_dict:
            return [my_dict[sub], index]
        
        my_dict[num] = index
    return []    #when not found
        


if __name__ == "__main__":
    
    nums = [2,7,11,15]
    #nums = [1,2,3,4]
    target = 5
    print(f"First set of nums: {nums} and target is: {target}")
    
    answer=find_target(nums, target)
    print(f"indexes are: {answer}")
    
    nums2 = [3,2,4]
    target2 = 6
    
    print(f"Second set of nums: {nums2} and target is: {target2}")
    answer2=find_target(nums2, target2)
    print(f"indexes are: {answer2}")
    
    nums3 = [3,3]
    target3 = 6
    
    print(f"Second set of nums: {nums3} and target is: {target3}")
    answer3=find_target(nums3, target3)
    print(f"indexes are: {answer3}")
    
    ###trying short code
    #nums = [2,7,11,15]
    #target = 9
    
    print(f"Second short code method with First set of nums: {nums} and target is: {target}")
    
    answer=find_target_second_option(nums, target)
    print(f"New short code method return indexes: {answer}")
    
    
    
    
    