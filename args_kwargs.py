def sum(*args, **kwargs) -> int:
    sum_is = 0
    for arg in args:
        sum_is += arg
        
    read_flag = kwargs.get("verbose", False) #read the flag and if it is not set then set to default False
    print(f"flag is: {read_flag}")    
        
    return sum_is    
        
        




if __name__ == "__main__":
    print("Hello args and kwargs")
    
    print(sum(10,20,30))
    
    print(sum(50,50, verbose=True))