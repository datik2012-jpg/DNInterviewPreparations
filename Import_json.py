import json
from Exceptions import total__duration_return_dict
import sys


def load_jobs(file_path: str) -> list | None:
    print('Load json from file started')
    try:
        with open(file_path, "r", encoding="utf-8") as file:
          data = json.load(file)
          if not isinstance(data, list):
              print(f"Expected to have list in hte file: {file_path} but there another format")
              return None
           #when list exist but inside the list we need to check we haev only dictionaries and not broken content
          for index, job in enumerate(data):
            if not isinstance(job, dict):
              print(f"Expected a dictionary at index {index} in the file {file_path}")
              return None
          
          return data
    except FileNotFoundError:
        print(f"File with json has not been found at: {file_path}")        
    
        return None
    except json.decoder.JSONDecodeError:
        print(f"Illegal json file or broken: {file_path}  please chech it's content")
        return None
    


if __name__ == "__main__":
    #print("hello")
    
    
    jobs_in_list=load_jobs("jobs.json")
    if (jobs_in_list is None):
        print("Exit from the program - json file has not found")
        sys.exit(1) 
    #print(jobs_in_list)
    
    print(total__duration_return_dict(jobs_in_list))
    
    
    #Следующее задание: файл существует, но содержит неправильный JSON:
    # [
    # {"name": "tests", "status": "failed",}
    # ]
    
    # jobs_in_list2=load_jobs("jobs_with_error.json")
    # if (jobs_in_list2 is None):
    #     print("Exit from the program - json file has not found or broken")
    #     sys.exit(1) 
    # #print(jobs_in_list)
    
    # print(total__duration_return_dict(jobs_in_list2))
    
    
    #Следующий случай: файл содержит корректный JSON, но вместо списка там словарь:
    #{"name": "tests", "status": "failed"}
    
    jobs_in_list3=load_jobs("jobs_dict_instead_of_list.json")
    if (jobs_in_list3 is None):
        print("Exit from the program - json file has issue it is dictionary")
        sys.exit(1) 
        #print(jobs_in_list)
        
    print(total__duration_return_dict(jobs_in_list3))