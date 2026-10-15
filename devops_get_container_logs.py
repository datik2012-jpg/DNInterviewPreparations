# Следующим шагом я предлагаю практику Python для автоматизации Windows/Linux — такие упражнения встречались в найденных отзывах об интервью Rafael.
# Начнём с небольшой задачи, используя знакомый тебе subprocess:
# Напиши функцию get_container_logs(container_name: str) -> dict, которая:
# 1. Получает последние 100 строк логов через docker logs --tail 100.
# 2. Возвращает returncode, stdout, stderr.
# 3. Обрабатывает отсутствие команды docker и таймаут в 5 секунд.
# Python запускается на Windows, контейнер — Linux в Docker Desktop. Какой список аргументов ты передашь в subprocess.run()?


import subprocess

#write a method which checks all running containers
def get_all_running_docker_containers() -> list:
    
    containers_list = []
    result = subprocess.run(
    ["docker", "ps", "--format", "{{.ID}}"],
    capture_output=True,
    text=True,
    timeout=5
)

    print(f"Status of the cmd is: {result.returncode}")
    print(f"All containers : \n{result.stdout}")
    
    #print(f"print each found container:")
    for container in result.stdout.splitlines():
        #print(container)
        containers_list.append(container)
        
    
    return containers_list

def get_container_logs(container_name: str):
    
    
  result =  subprocess.run(
    ["docker", "logs", "--tail", "100", container_name],
    capture_output=True,
    text=True,
    timeout=5
)
  print(f"show code: {result.returncode}")
  print(f"show ERROR: {result.stderr}")
  print(f"show stdout: {result.stdout}")
  
  return result.stdout


if __name__ == "__main__":
    print("Get container logs task:")
    
    
    #logs=get_container_logs("70789fc6c805")  #we send container name of bmcpolinexo - frontend or backend
    #print(f"STDOUT is empty: {logs}")
    
    
    #find all running container and put their ID (nmaes) to the list
    print("Print all containers:")
    all_containers = get_all_running_docker_containers()
    print(f"all docker existing containers are: {all_containers}")
    
    
    #run over found container and grab his logs
    for container in all_containers:
        print(f"Print logs from container: {container}")
        logs=get_container_logs(container)  #we send container name of bmcpolinexo - frontend or backend
        print(f"STDOUT is empty: {logs}")
    