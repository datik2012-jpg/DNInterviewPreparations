import subprocess


def run_command(command: list[str]) -> dict:
    
    try:
      result = subprocess.run(command, capture_output=True, text=True, timeout=5)
      #print(result.stdout.strip())
      
    except subprocess.TimeoutExpired:
      return {
          "returncode": None,
          "stdout": "",
          "stderr": "timeout 5 sec reached when running subprocess command"
      }
    except FileNotFoundError:
        return {
          "returncode": None,
          "stdout": "",
          "stderr": f"command which we get is: {command[0]}  has not found and that caused to the fail"
        }    
    
    
    return {
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),               
    }


if __name__ == "__main__":
    print("First command:")
    my_dict = run_command(["python", "--version"])
    print(my_dict)
    
    print("Second command - test interupt exit code 2:")
    print(run_command([
    "python", "-c",
    "import sys; print('Build failed', file=sys.stderr); sys.exit(2)"
     ]))
    
    print("Timeout test:")

    result = run_command([
        "python",
        "-c",
        "import time; time.sleep(10)",
    ])
    
    print(result)
    
    print("Command not found - test:")
    print(run_command(["definitely_missing_command_123"]))
    
    
    #how to loop over list with dictinary
    
    #for job in jobs:                 # Каждый элемент списка — словарь
    #for key, value in job.items():  # Каждая пара внутри словаря
        #print(key, value)
        
    durations = {
    "build": 120,
    "tests": 45,
    "deploy": 20,
    }
    
    for key, value in durations.items():
        if value > 30:
          print(key, value)    
