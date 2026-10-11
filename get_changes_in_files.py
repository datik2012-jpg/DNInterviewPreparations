import subprocess


def get_changed_configs(current_branch: str, remote_branch: str, command="git diff --name-only") -> list[str]:
    full_command = command + " " + remote_branch + " " + current_branch
    result = subprocess.run(full_command, capture_output=True, text=True, timeout=5)
    print(result.stdout.strip())


if __name__ == "__main__":
    print("hello")
    #git diff --name-only main feature/test
    
    #get_changed_configs("git diff --name-only BASE HEAD")
    #exlain we want to see only files name changes between REMOTE main branch and my local feature/test branch
    get_changed_configs("origin/main", "feature/test")