import sys

def _exit():
    sys.exit(0)
    
COMMANDS = {
    'exit': _exit,
}

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()
        if command in COMMANDS.keys():
            COMMANDS.get(command)()
        else:
            sys.stdout.write(f'{command}: command not found\n')
        sys.stdout.flush()
        


if __name__ == "__main__":
    main()
