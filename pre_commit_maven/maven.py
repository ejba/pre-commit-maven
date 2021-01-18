import argparse
import os.path
from pre_commit_maven.utils import maven
from pre_commit_maven.utils import generic_main

CWD = os.getcwd()


def main(argv: list, cwd=CWD, print_fn=print, execute_fn=generic_main.execute) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("goals", nargs="*", help="maven goals to run")
    args = parser.parse_args(argv)

    if not any(args.goals):
        parser.error("No goals provided.")
        return 1

    return execute_fn(args.goals, cwd)


if __name__ == "__main__":
    exit(main())
