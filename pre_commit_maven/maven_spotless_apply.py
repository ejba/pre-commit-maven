import argparse
import os
import os.path
from pre_commit_maven.utils import generic_main
from pre_commit_maven.utils import shell

CWD = os.getcwd()
ENV = os.environ.copy()

def main(cwd=CWD, print_fn=print, execute_fn=generic_main.execute) -> int:
    result = execute_fn(["spotless:apply"], cwd)
    # Important that following command is MODIFIED filter only!
    modified_files =  shell.execute_direct("git diff --cached --name-only --diff-filter=M | tr '\n' ' '| rev | cut -c 2- | rev", cwd=cwd, env=ENV)
    if modified_files.stdout != '':
        shell.execute_direct("git add " + modified_files.stdout)
        result = shell.execute_direct("git commit -m \"spotless apply auto-commit\"")
        return result
    return result


if __name__ == "__main__":
    exit(main())
