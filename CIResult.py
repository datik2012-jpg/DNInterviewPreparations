

def get_failed_jobs(jobs_list: list) -> list:
    
    print("Just detect by status")
    list_failed_jobs = []
    
    for job in jobs_list:
        #print(job)
        if job["status"] == "failed":
            list_failed_jobs.append(job["name"])
    #print(list_failed_jobs) 
    
    return list_failed_jobs           
            
def detect_with_no_status(jobs_list: list) -> list:
    print("Detect when no status")
    list_failed_jobs = []
        
    for job in jobs_list:
        #print(job)
        if job.get("status") == "failed":  # just this can work cause if no status condition will be skipped
            list_failed_jobs.append(job["name"])
        
    #print(list_failed_jobs)    
    return list_failed_jobs  

def new_func_handling_no_stage_name(jobs3_list: list) -> list:
    
    print("Detect when no name in the dictionary and do not to fail to append")
    list_failed_jobs = []
            
    for job in jobs3_list:
        #print(job.get("name")) return None when name not exsit and when name exist return it's name 
        #И маленькое уточнение к комментарию: get() возвращает None и когда ключ отсутствует, и когда ключ существует со значением None
        if job.get("status") == "failed" and job.get("name"):  # just this can work cause if no status condition will be skipped
            list_failed_jobs.append(job["name"])
            
    #print(list_failed_jobs)    
    return list_failed_jobs 


def failed_jobs_duration(jobs: list) -> str:
    #75  # tests: 45 + security: 30
    print("Sum duration for all failed jobs")
    list_failed_jobs = []
    failed_dict = {}
    counter_failed_duration = 0
    
    for job in jobs:
        if job.get("status") == "failed" and job.get("name"):
            #list_failed_jobs.append({job["name"]:job["duration"]})
            failed_dict[job["name"]] = job.get("duration", 0) #in case when no duration we will set 0 as default
            counter_failed_duration += job.get("duration", 0)
            #print(counter_failed_duration)
    
    return str(counter_failed_duration) + "#" + " " + " ".join(f"{key} {value}" for key, value in failed_dict.items())     
    
    


if __name__ == "__main__":
    #print("hello")
    
    jobs = [
    {"name": "build", "status": "success", "duration": 120},
    {"name": "tests", "status": "failed", "duration": 45},
    {"name": "security", "status": "failed", "duration": 30},
    {"name": "deploy", "status": "success", "duration": 20},
    ]
    
    list_of_failed_jobs=get_failed_jobs(jobs)
    #list_of_failed_jobs=get_failed_jobs([]) #empty list check
    print(list_of_failed_jobs)
    
    # next task if no status - method should not to fail
    
    jobs2 = [
    {"name": "build", "status": "success"},
    {"name": "tests", "status": "failed"},
    {"name": "deploy"},
    ]
    
    list_of_failed_jobs_even_if_no_status = detect_with_no_status(jobs2)
    print(list_of_failed_jobs_even_if_no_status)
    
    
    #Q: What will happen with method if we send only: {"status": "failed"}
     #A: we will get KeyError: 'name'
     
     #Now change the code if we do not have name in the dictionary
     
    jobs3 = [
    {"name": "build", "status": "success"},
    {"name": "tests", "status": "failed"},
    {"name": "deploy"},
    {"status": "failed"},    
        
    ]
    
    list_skipped_no_name_job = new_func_handling_no_stage_name(jobs3)
    print(list_skipped_no_name_job)
    
    #Следующее задание: напиши функцию, которая возвращает суммарную длительность только failed jobs:
    #example: 75  # tests: 45 + security: 30
    list_sum_duration_of_failing_jobs = failed_jobs_duration(jobs)
    print(list_sum_duration_of_failing_jobs)
    