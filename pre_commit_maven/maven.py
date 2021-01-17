from __future__ import print_function

import argparse
import os.path
from pre_commit_maven.utils import maven
from pre_commit_maven.utils import generic_main

CWD = os.getcwd()


def main(argv: list, cwd=CWD, print_fn=print) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("goals", nargs="*", help="maven goals to run")
    args = parser.parse_args(argv)

    if args.goals is None or len(args.goals) == 0:
        print_fn("goals not specified")
        return 1

    return generic_main.execute(args.goals, cwd)


if __name__ == "__main__":
    exit(main())
