import os
import sys

PATH_LIST  = os.environ.get("PATH", "").split(os.pathsep)


def NOTFOUND(command: str):
    sys.stdout.write(f'{command}: command not found')

def _exit(_):
    sys.exit(0)
    
def _echo(args: list):
    for arg in args:
        sys.stdout.write(arg + " ")
    sys.stdout.write("\n")

def _type(args: list):
    if len(args) == 0:
        sys.stdout.write("type: missing argument")
    elif len(args) > 1:
        sys.stdout.write("type: too many arguments")
    else:
        args = args[0]
        if check_command(args):
            message = f"{args} is a {COMMANDS.get(args)[1]}"
            sys.stdout.write(message)
            sys.stdout.write("\n")
            return
        is_found, full_path = check_command_in_path(args)
        if is_found:
            sys.stdout.write(f"{args} is {full_path}")
        else:
            sys.stdout.write(f"{args}: not found")
    sys.stdout.write("\n")

COMMANDS = {
    'exit': (_exit, 'shell builtin'),
    'echo': (_echo, 'shell builtin'),
    'type': (_type, 'shell builtin'),
    
}

def check_command(command: str):
    if command in COMMANDS.keys():
        return True
    else:
        return False
    
def check_command_in_path(command: str):
    for root_path in PATH_LIST:
        for dirpath, dirnames, filenames in os.walk(root_path):
            for filename in filenames: 
                filename_no_ext, ext = os.path.splitext(filename)
                if command == filename_no_ext:
                    full_path = os.path.join(dirpath, filename)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        return True, os.path.splitext(full_path)[0]
                    
    return False, None

    
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip()
        command = user_input.split()[0]
        args = user_input.split()[1:]
        if check_command(command):
            COMMANDS.get(command)[0](args)
            
        else:
            NOTFOUND(command)
            sys.stdout.write("\n")

        sys.stdout.flush()
        


if __name__ == "__main__":
    main()
