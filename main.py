import os
import subprocess
import logo
ver = "0.1.0"
def startup():
    os.chdir(os.path.expanduser('~'))
    clear_screen()
    print(logo.name)

def echo(echoq):
    print(input(f"{echoq}:   "))
def cd():
    try:
        to = input("Enter dir name:   ")
        os.chdir(to)
        print(f"Changed directory to: {os.getcwd()}")
    except (FileNotFoundError,NotADirectoryError):
        print('Not a real destination')

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)


def ls():
    try:
        items = os.listdir('.')
        if not items:
            print("[Empty]")
            return

        print(f"Content of: {os.getcwd()}\n")
        print(f"{'NAME':<30} {'TYPE':<10}")
        print("-" * 40)

        for item in items:
            if os.path.isdir(item):
                typ = "[DIR]"
            else:
                typ = "[FILE]"
            print(f"{item:<30} {typ:<10}")

    except Exception as e:
        print(f"Error reading directory: {e}")
startup()
while True:
    print("=" * 40)
    print(f"[e] Echo\t[cd] Change Directiory\t[q] Quit\t[ver] Show current version\n[clr] Clear Screen\t[ls] List Directory")
    print("=" * 40)
    answer = input("Pick a Command:   ").lower().strip()

    if answer == "ver":
        print(ver)
    elif answer == "e":
        echo("Echo")
    elif answer == "cd":
        cd()
    elif answer == "q":
        break
    elif answer == "clr":
        clear_screen()
        print(logo.name)
    elif answer == "ls":
        ls()
    else:
        print("Unknown command")