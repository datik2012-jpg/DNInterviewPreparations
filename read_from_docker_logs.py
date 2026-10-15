import subprocess

#docker logs --tail 10 8da405a3523d  - in case we know the docker container id

def start_read_docker_logs():
    
    result = subprocess.run(
        ["docker", "logs", "--tail", "20", "8da405a3523d"],
        capture_output=True,
        text=True,
        timeout=5,
        
    )
    
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strim())
   
    for line in (result.stdout + "\n" + result.stderr).splitlines():
        if "ERROR" in line:
            print(f"ERROR in line: {line}")
        else:
            print(line)    
             

if __name__ == "__main__":
    print("Read from Docker logs:")
    
    start_read_docker_logs()