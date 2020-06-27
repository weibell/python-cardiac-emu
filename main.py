from argparse import ArgumentParser

from cardiac import Cardiac

if __name__ == "__main__":
    parser = ArgumentParser(description="CARDIAC interpreter written in Python")
    parser.add_argument("program", type=str, help="Program")
    args = parser.parse_args()

    with open(args.program) as f:
        program = [line.strip() for line in f]

    cardiac = Cardiac()
    cardiac.load(program)
    output = cardiac.run()
    print("\n".join(output))
