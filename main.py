import sys

from Cardiac import Cardiac

if __name__ == "__main__":
    program_file = sys.argv[1]
    with open(program_file) as f:
        program = [line.strip() for line in f]

    cardiac = Cardiac(program)
    output = cardiac.run()
    print("\n".join(output))
