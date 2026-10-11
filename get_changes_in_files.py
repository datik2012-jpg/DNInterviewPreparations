import subprocess


def get_changed_configs(base: str, head: str) -> list[str]:
    resutl = subprocess.run(command, capture_output=True, text=True, timeout=5)


if __name__ == "__main__":
    print("hello")
    get_changed_configs("git diff --name-only BASE HEAD")