
def jewels_check_in_stones(jewels, stones) -> int:
    
    jew_set = set(jewels) # add jewels tot he set
    count_jew = 0
    for stone in stones: #loop over each stone 
        if stone in jew_set:
            count_jew +=1
    return count_jew        


if __name__ == "__main__":
    print("Jewels stones task:")
    
    #Следующая задача на set — Jewels and Stones:
    #Каждый символ — отдельный камень. Здесь подходят a, A, A. Регистр важен: a и A — разные символы.
    jewels = "aA"       # какие символы считаются драгоценностями
    stones = "aAAbbbb"  # твои камни

    # Ответ: 3
    
    answer=jewels_check_in_stones(jewels, stones)
    print(f"Answer is: {answer}")