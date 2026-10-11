


def parse_duration(num):
    
    try:
        return int(num)
            
        
    except (ValueError, TypeError):
        
        
        return 0   
            
                
def total_duration(jobs: list):
    print("started sum duration")
    list_dict_failed_job_failed = []
    total_duration = 0
    
    for job in jobs:
        if job.get("status") == 'failed':
            
            dict_failed_job = {}
            
            dict_failed_job["name"] = job.get("name")
            
            parsed_duration = parse_duration(job.get("duration"))
            
            dict_failed_job["duration"] = parsed_duration
            
            total_duration += parsed_duration
            
            list_dict_failed_job_failed.append(dict_failed_job)
    
    #for jj in list_dict_failed_job_failed:
        #print(jj) 
    return str(total_duration)           
                        

def total__duration_return_dict(jobs: list) -> dict:
    print("started sum duration failed jobs with return full dictionary")
    response_dict = {"total_duration": 0, "failed_jobs": []}
    
    for job in jobs:
        if job.get("status") == "failed":
            #print(job)
            parsed_duration = parse_duration(job.get("duration")) #we get int from the parser
            job_name = job.get("name") or "unknown" # if name not exsit or it None or it is "" (empty string) it will set "unkown"
            
            response_dict["total_duration"] += parsed_duration  # # Add parsed duration to the running total
            response_dict["failed_jobs"].append({"name": job_name, "duration": parsed_duration })
    return response_dict

if __name__ == "__main__":
    #print("hello sir")
    
    jobs = [
        {"name": "build", "status": "success", "duration": 120},
        {"name": "tests", "status": "failed", "duration": 45},
        {"name": "security", "status": "failed", "duration": 30},
        {"name": "deploy", "status": "success", "duration": 20},
        ]    
    

    
    
#Следующее маленькое задание: напиши функцию parse_duration(value),
# которая возвращает число для 45 и "45", а для "unknown" возвращает 0. Используй int() и try/except ValueError.  

print("Try and Exception for number and string and unknown")
print(parse_duration(45)) 
print(parse_duration("45"))  
print(parse_duration("unknown")) 


#Здесь int(None) вызовет TypeError, а твой except ValueError его не перехватит.
#Измени функцию так, чтобы она возвращала 0 и при ValueError, и при TypeError. Как запишешь except для двух типов ошибок?
print("Added TypeError option to exception:")
print(parse_duration(None)) 




###################################################################
jobs2 = [
    {"name": "build", "status": "success", "duration": 120},
    {"name": "tests", "status": "failed", "duration": "45"},
    {"name": "security", "status": "failed", "duration": None},
    {"name": "deploy", "status": "failed"},
    {"status": "failed", "duration": 10}, #job without the name
]

#Следующий шаг: используй parse_duration() внутри функции суммирования длительностей failed jobs.
str_final_sum_and_task_name_and_duration=total_duration(jobs2)
print(f"total duration for failed job is: {str_final_sum_and_task_name_and_duration}")   



# Следующее задание: верни из функции и сумму, и список failed jobs в одном словаре:
# Example:
# {
#    "total_duration": 45,
#    "failed_jobs": [
#        {"name": "tests", "duration": 45},
#        {"name": "security", "duration": 0},
#        {"name": "deploy", "duration": 0},
#     ],
# }
print(total__duration_return_dict(jobs2))


#test when we pass empty list

jobs_empty = []
print("test empty list")
print(total__duration_return_dict(jobs_empty))