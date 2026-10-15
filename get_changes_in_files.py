

import subprocess


# def get_changed_configs(current_branch: str, remote_branch: str, command="git diff --name-only") -> list[str]:
#     full_command = command + " " + remote_branch + " " + current_branch
#     result = subprocess.run(full_command, capture_output=True, text=True, timeout=5)
#     print(result.stdout.strip())


def get_changed_configs2(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", base, head],
        capture_output=True,
        text=True,
        timeout=5,
    )
    
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    
    
    
    change_configs = [] # create empty list for next usage - add later only configs which we need 
    
    # Здесь добавь фильтрацию result.stdout.splitlines() 
    for path in result.stdout.splitlines():
        #print(path)
        
        if path.startswith("configs/") and path.endswith((".yaml", ".yml")):
            change_configs.append(path)
    
    return change_configs

if __name__ == "__main__":
    print("hello")
    #git diff --name-only main feature/test
    
    #get_changed_configs("git diff --name-only BASE HEAD")
    #exlain we want to see only files name changes between REMOTE main branch and my local feature/test branch
    # get_changed_configs("feature/test", "origin/main")
    
    #better way to do  it - new meathod
    print(get_changed_configs2("origin/main", "feature/test"))