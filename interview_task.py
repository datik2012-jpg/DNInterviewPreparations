


# You are given an array of integers nums and an integer target, return indices of # the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not # # use the same element twice.
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







#NOT WORKING CODE
# def my_func(nums: list, target: int) -> list:
#     answer = []
#     first = 0
#     last = len(nums) -1 
#     my_dict = {}
#     for num in nums[first:]:
#         #print(num)
#         my_dict[num] = first
#         sub = target - num # 9 - 2 = 7
#         if sub in my_dict.keys():
#             answer.append(my_dict[sub])
#             answer.append(first)#my_dict.items():
#         first +=1  
#     return answer 


def find_target_in_nums(my_nums: list, target: int) -> list:
    my_dict = {}
    print(f"Print my_nums: {my_nums}")
    i = 0
    final_list = []
    for num in nums:
        #print(num)
        my_dict[num] = i
        #i += 1
        #check if key exist in the dictionary and if exist we found two indexes!!
        sub = target - num  # 9 - 2 = 7
        print(f" sub is {sub} = {target} - {num}")
        
        if sub in my_dict.keys():
            print(f"we do have a key for sub {sub}")
            get_index = my_dict[sub] # toget an index of the number
            print(f"index is: {get_index}")
            if get_index != i:
                final_list.append(get_index)
                final_list.append(my_dict[num])
                break
            
        else:
            print(f"sub {sub} is not in the dicionary {my_dict}")    
        i += 1
    print(my_dict)    
        
        
    
    
    return final_list   




if __name__ == "__main__":
    
    #nums = [2,7,11,15]
    #target = 9
    #answer = []
    fist = 0
    #last = len(nums) -1 
    #my_dict = {}
    
    #nums = [3,2,4]
    #target = 6
 
    #not fully working code - FAILED
    #print(my_func(nums, target))  
    
    
    print("Trying another solution:")
    #nums = [2,7,11,15]
    #target = 9 
    
    nums = [3,2,4]
    target = 6
    
    #nums = [1, 4, 9 , 6 , 4, 2]
    #target = 7
    
    print(f" final list is: {find_target_in_nums(nums, target)}")


