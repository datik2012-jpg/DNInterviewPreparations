
def intersection(nums1: list, nums2: list) -> set:
    
    first_set = set()
    second_set = set()
    
    for num in nums1:
        first_set.add(num)
        
    for num in nums2:
        second_set.add(num)
        
    #tricks with set:
    
    #sub_set = first_set - second_set # {1}
    #sub_set = first_set | second_set # Combines items from both sets. {1, 2, 3, 4}
    #sub_set = first_set ^ second_set #Keeps elements that are in one of the sets, but not both (the opposite of intersection) {1, 4}
    #In-Place Updates (|=, &=, ^=, -=)
    #my_set = {1, 2, 3}
    #my_set -= {3, 4} 
    #print(f"my_set:{my_set}") # |= will do merge {1, 2, 3, 4} , &= find if both have the same {3}, ^= will give {1, 2, 4} - substarct common, -=  - from first substract second (what is only in second will not be taken) {1, 2}
    #sub_set = first_set & second_set
    #sub_set = first_set & second_set
    #sub_set = first_set & second_set
    
    sub_set = first_set & second_set #Keeps only elements found in both sets.  {2, 3} #Оператор & находит пересечение — значения, которые есть в обоих множествах:
       
        
        
    print(f"both sets are: {first_set} {second_set}") 
    print(f"sub of two sets are: {sub_set}") 
    
    #return list(set(nums1) & set(nums2))    return list and do & in the same moment
    return list(sub_set)        
        
        
    



if __name__ == "__main__":
    print("Intersections of two Arrays!!")
    
    
#Давай следующую задачу на set — LeetCode 349: Intersection of Two Arrays.
#Даны два списка. Нужно вернуть общие числа без повторений. Порядок ответа любой.

nums1 = [1, 2, 2, 3]
nums2 = [2, 2, 3, 4]

#nums1 = [1, 2, 2]
#nums2 = [2, 2, 2]

# Ответ: [2, 3]


inter = intersection(nums1, nums2)
print(f"Intersection is: {inter}")
