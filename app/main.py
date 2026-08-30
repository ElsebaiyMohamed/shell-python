import sys

def _exit(_):
    sys.exit(0)
    
def _echo(args: list):
    for arg in args:
        sys.stdout.write(arg + " ")
    sys.stdout.write("\n")

COMMANDS = {
    'exit': _exit,
    'echo': _echo,
}

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip()
        command = user_input.split()[0]
        args = user_input.split()[1:]
        if command in COMMANDS.keys():
            COMMANDS.get(command)(args)
        else:
            sys.stdout.write(f'{command}: command not found\n')
        sys.stdout.flush()
        


if __name__ == "__main__":
    main()
