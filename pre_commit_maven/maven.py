import argparse
import os.path
from pre_commit_maven.utils import maven

CWD = os.getcwd()


def main(argv: list, cwd=CWD, print_fn=print) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("goals", nargs="*", help="maven goals to run")
    args = parser.parse_args(argv)

    if args.goals is None or len(args.goals) == 0:
        print_fn("goals not specified")
        return 1

    execution_result = maven.execute_goals(args.goals, cwd)
    if execution_result.return_code != 0:
        maven.print_error(execution_result)

    return execution_result.return_code


if __name__ == "__main__":
    exit(main())
