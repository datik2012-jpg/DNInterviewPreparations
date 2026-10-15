

def contains_duplicates(nums: list) -> bool:
    
    seen = set() #create a set which can not add the same value , only once
    for num in nums:
        #print(f"{num}")
        seen.add(num)
        
        
    #print(f"seen len is: {len(seen)} and nums len is: {len(nums)}")
    #if 0 in seen: #how to check in number exist in the set
       # print("zero in seen")
        
    if len(seen) == len(nums):
        return False
    else:
        return True
    
    #or
    #return len(seen) != len(nums)
    
    
def contains_duplicates_improved_algo(nums) -> bool:
    
    seen = set() #create empty set
    
    for num in nums:
        #print(f"{num}")
        
        #improved part before we add we check if the number already exist in the set so we do not need ot run all set and can cut in the middle :-)
        if num in seen:
            return True
        seen.add(num)
        
    return False # we finished all the loop and din't find duplicates    
        
           

if __name__ == "__main__":
    print("Contains duplicates question!!")
    
    #Возьмём LeetCode Contains Duplicate:
    #Дан список чисел. Верни True, если какое-нибудь число встречается хотя бы дважды. Иначе верни False.
    #nums = [3, 1, 7, 3]  # True
    nums = [3, 1, 7, 2]  # False
    
    contains = contains_duplicates(nums)
    print(f"Contains duplicates True\False: {contains}")
    
    
    #Теперь попробуем улучшение: твой код всегда проходит весь список. А для [3, 3, 1, 7, 9] мы уже на втором числе знаем ответ.
    #Какую проверку нужно поставить перед seen.add(num), чтобы сразу вернуть True, если число уже встречалось?
    print(f"Imporved algorithm:")
    contains_improved = contains_duplicates_improved_algo(nums)
    print(f"Contains duplicates True\False: {contains_improved}")
    