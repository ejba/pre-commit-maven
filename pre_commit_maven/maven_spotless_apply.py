import argparse
import os.path
from pre_commit_maven.utils import maven

CWD = os.getcwd()


def main(cwd=CWD, print_fn=print) -> int:
    execution_result = maven.execute_goals(["spotless:apply"], cwd)
    if execution_result.return_code != 0:
        maven.print_error(execution_result)

    return execution_result.return_code


if __name__ == "__main__":
    exit(main())
