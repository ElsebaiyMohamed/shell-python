import sys

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
        else:
            NOTFOUND(args)
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
