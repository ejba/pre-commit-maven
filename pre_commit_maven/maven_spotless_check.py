import argparse
import os.path
from pre_commit_maven.utils import generic_main

CWD = os.getcwd()


def main(cwd=CWD, print_fn=print) -> int:
    return generic_main.execute(["spotless:check"], cwd)


if __name__ == "__main__":
    exit(main())
