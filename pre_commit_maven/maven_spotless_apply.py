import argparse
import os.path
from pre_commit_maven.utils import maven

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


def main(cwd=CURRENT_DIR, print_fn=print) -> int:
    execution_result = maven.execute_goals(["spotless:apply"], cwd)
    if execution_result.return_code != 0:
        print_fn(execution_result.stdout)

    return execution_result.return_code


if __name__ == "__main__":
    exit(main())
