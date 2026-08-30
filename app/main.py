import sys

COMMANDS = {}

def main():
    while True:
        sys.stdout.write("$ ")
        command = sys.stdin.readline().strip()
        if command in COMMANDS:
            pass
        else:
            sys.stdout.write(f'{command}: command not found\n')
        


if __name__ == "__main__":
    main()
