#run from the terminal: python .\argparse_usage_for_diff.py --base origin/main --head features/test --timeout 5
from get_changes_in_files import get_changed_configs2

import argparse





if __name__ == "__main__":
    print("Use argparse - when user send us parameters in the command line and we want to catch them and use")
    print("When user run somethoing like: python .\\argparse_usage_for_diff.py --base origin/main --head feature/test --timeout 5")
    
    parser = argparse.ArgumentParser(description="Find changes in configuration files")
    
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--timeout", default=5, type=int) #we can pass it for the subprocess
    
    args = parser.parse_args()
    print(f"base: {args.base}, head: {args.head}, timeout: {args.timeout}")
    
    print(get_changed_configs2(args.base, args.head))
    
    #Full output: 
    # (.venv) PS D:\GitHub\DNInterviewPreparations> python .\argparse_usage_for_diff.py --base origin/main --head feature/test --timeout 5 
    # Use argparse - when user send us parameters in the command line and we want to catch them and use
    # When user run somethoing like: python .\argparse_usage_for_diff.py --base origin/main --head feature/test --timeout 5
    # base: origin/main, head: feature/test, timeout: 5
    # ['configs/app.yaml', 'configs/network.yaml']