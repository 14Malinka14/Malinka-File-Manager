import os
import subprocess
os.chdir(os.path.expanduser('~'))
ver = "0.0.1"
def echo(echoq):
    print(input(f"{echoq}:   "))
def cd():
    try:
        to = input("Enter dir name:   ")
        os.chdir(to)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
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
clear_screen()
print("=" * 40)
print(r"""    __  ___      ___       __            _______ __        __  ___                                 
   /  |/  /___ _/ (_)___  / /______ _   / ____(_) /__     /  |/  /___ _____  ____ _____ ____  _____
  / /|_/ / __ `/ / / __ \/ //_/ __ `/  / /_  / / / _ \   / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 / /  / / /_/ / / / / / / ,< / /_/ /  / __/ / / /  __/  / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/  /_/\__,_/_/_/_/ /_/_/|_|\__,_/  /_/   /_/_/\___/  /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                                                /____/             """)
while True:
    print("=" * 40)
    print(f"[e] Echo\t[cd] Change Directiory\t[q] Quit\t[ver] Show current version\n[clr] Clear Screen\t[ls] List Directory")
    print("=" * 40)
    answer = input("Pick an Command:   ").lower().strip()

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
        print(r"""    __  ___      ___       __            _______ __        __  ___                                 
   /  |/  /___ _/ (_)___  / /______ _   / ____(_) /__     /  |/  /___ _____  ____ _____ ____  _____
  / /|_/ / __ `/ / / __ \/ //_/ __ `/  / /_  / / / _ \   / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ ___/
 / /  / / /_/ / / / / / / ,< / /_/ /  / __/ / / /  __/  / /  / / /_/ / / / / /_/ / /_/ /  __/ /    
/_/  /_/\__,_/_/_/_/ /_/_/|_|\__,_/  /_/   /_/_/\___/  /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                                                /____/             """)
    elif answer == "ls":
        clear_screen()
        ls()
    else:
        print("Unknown command")