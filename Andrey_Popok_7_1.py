from platform import architecture, machine, node, platform, processor, python_build, python_compiler, python_implementation, python_version, python_version_tuple, win32_ver
from typing import Match

def main():
    while True:
        value = input("Choose the info you need: ")
        match value: 
            case "processor":
                print(processor())
                print(architecture())
            case "os":
                print(platform(0))
                print(win32_ver())
            case "python":
                print(python_build())
                print(python_compiler())
                print(python_implementation())
                print(python_version())
            case "exit":
                break
            case _:
                print("Your choice is not recognized, please try again.")

main()