#! /usr/bin/env python3
import subprocess
import sys
import os

def main():
    # get all command arguments
    args = sys.argv
    
    # pass through the arguments to the docker command, docker run ...
    subprocess.run(["docker", "run", *args[1:]], check=True)
    
    # get --name argument
    name_index = args.index("--name")
    name = args[name_index + 1]
    name_ascii_hex = name.encode('ascii').hex()
    
    # open vscode in the container
    os.system(f"code --folder-uri vscode-remote://attached-container+{name_ascii_hex}/workspace")

if __name__ == "__main__":
    main()