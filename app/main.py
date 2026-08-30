import sys

COMMANDS = {}

def main():
    sys.stdout.write("$ ")
    command = sys.stdin.readline().strip()
    if command in COMMANDS:
        pass
    else:
        sys.stdout.write(f'{command}: command not found')
        


if __name__ == "__main__":
    main()
