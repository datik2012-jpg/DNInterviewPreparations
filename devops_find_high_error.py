
def unhealthy_services(logs: list[tuple[str, int]], treshold: float) -> list[str]:
    dict_status_count = {}
    dict_count_service = {}
    answer_treshold_services = []
    for api in logs:
        print(f"api is: {api[0]} {api[1]}")
        
        #count how much time the same service apper in the list - later we need it to callculate a thrashold
        if api[0] in dict_count_service:
            dict_count_service[api[0]] += 1
        else:
            dict_count_service[api[0]] = 1
                
        #treat status codes as errors
        if 500 <= api[1] <= 599: # error code
            if api[0] in dict_status_count and dict_status_count[api[0]] != None: # check if if service already in the dictionary 
                print(f"key: {api[0]}")
                dict_status_count[api[0]] += 1  #counter up ,cause we want to count all service erorrs for calculation later
            else: #when service is not in the dictionary yet
                dict_status_count[api[0]] = 1  # counter starts from ZERO 
        elif 200 <= api[1] <= 499: #if status between this ranges and we need to check service already not exist in the dictionary - then set to None
            if api[0] not in dict_status_count:
                dict_status_count[api[0]] = None        
                
    #now when we have a data we need to calculate treshold and compare to given treshold
    for key, value in dict_status_count.items():
        print(f"key value: {key} {value}")
        
        #when None no need to calculate BUT if the treshold set to 0 - means we need all services then we need to calclulate
        if value == None:
            calc_treshold = 0 #in case when user send treshhold 0 and should be calculated for all services
        else:
            #now we need to use second dictionary which has service and count   - and for the same service do calculation by value
            calc_treshold = dict_status_count[key] / dict_count_service[key]  # errors / total
            
        if calc_treshold >= treshold: 
            answer_treshold_services.append(key)               
    
    print(f"dictionary service and counters: {dict_status_count}") 
    print(f"count services apper in the log: {dict_count_service}")           
    return answer_treshold_services                


def unhealthy_services_2(logs: list[tuple[str,int]], treshold: float) -> list:
    error_counts = {} #one dictionary to count failure codes
    total_counts = {} # second dictionary to count all service - casue we need later to do math and calculate treshold
    unhealthy = []
    
    for service, code in logs:
        print(f"service {service }code {code}")
        
        
        total_counts[service] =  total_counts.get(service, 0) + 1 # we check if service already exist - if not exist set to 0 and add 1 , if service already exist in the dictionary so do +1 to the it's counter
        error_counts.setdefault(service, 0) # will set default when the service not added yet as ZERO  - count we will later 
        
        if  500 <= code <= 599: 
            error_counts[service] += 1 # increase the counter
            
            
    for service, count in total_counts.items():
        
        calc_treshold = error_counts[service] / count
        
        if calc_treshold >= treshold:
            unhealthy.append(service)
        
        
                      
            
    print(f"from better method print error_counts dict : {error_counts}")        
    print(f"from better method print total_counts dict : {total_counts}")
    
    return unhealthy    

if __name__ == "__main__":
    print("Find services with a high error rate")
    
    
    logs = [
    ("api", 200),
    ("api", 500),
    ("api", 503),
    ("auth", 200),
    ("auth", 401),
    ("worker", 500),
   ]
    
    # Requirements:
    # - Treat status codes 500–599 as errors.
    # - Calculate each service’s error rate: errors / total_requests.
    # - Return service names whose error rate is greater than or equal to threshold, sorted alphabetically.
    # - Return [] for empty logs.
    # - Assume threshold is between 0 and 1.
    # Example:
    # unhealthy_services(logs, 0.5)
    # # ["api", "worker"]
    # api has 2 errors out of 3 requests, worker has 1 out of 1, and auth has none.
    #Challenge: Process the logs in one pass before sorting the result.

    status= unhealthy_services(logs, 0.5)
    print(f"Current logs status is: {status}")
    
    print("Better version of the same solution with clean code:")
    status2 = unhealthy_services_2(logs, 0.5)
    print(f"Better code version so the Current logs status is: {status2}")