
def daily_temperatures(temperatures: list) -> list:
    #len_temp=len(temperatures)
    #print(f"Temperature length: {len_temp}")
    
    answer = [0] * len(temperatures)
    my_stack = []
    for index , temp in enumerate(temperatures):
        print(f"Index: {index} and temperature: {temp}")
        
        while my_stack and temperatures[my_stack[-1]] < temp: #if my_stack is not empty we need start to check if there we have smallest BUT we need to check as well if first POP (do peek my_stack[-1] - look the lates) is smaller then currrent temp[i] IF  POP() > temp[i] then just add
            j = my_stack.pop()  #getting the latest
            answer[j] = index - j  # put sbstraction of index so it will give us the distination
            
        
        #is stuck is empty add temp and if stuck has pop which large then current temp
        my_stack.append(index)
    return answer    
        
        



if __name__ == "__main__":
    print("Play with stack:")
    
    
    #stack = []
    
    #stack.append(10)
    #stack.append(20)
    #stack.append(30)
    
    
    #print(stack) # [10, 20, 30]
    
    
    #pop - the newest will get out
    
    #a=stack.pop()
    #print(a) # 30
    
    #print(stack)
    #[10, 20]
    
    
#Task:
        
#Давай LeetCode 739 — Daily Temperatures, уровень Medium. На ней хорошо тренируется стек.
#Дан список температур по дням. Для каждого дня нужно найти, через сколько дней будет более высокая температура. Если такого дня нет — записать 0.
#temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# ответ:       [ 1,  1,  4,  2,  1,  1,  0,  0]
    print("Task find first max temperature")
    #temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    temperatures = [69, 68, 67, 70]
    answer = daily_temperatures(temperatures)
    print("Answer print")
    print(answer)