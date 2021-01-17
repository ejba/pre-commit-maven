from pre_commit_maven.utils import shell
from pre_commit_maven.utils.shell import ExecutionResult


class Colours:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def execute_goals(goals: list, cwd: str, shell_runner=shell):
    assert goals is not None and len(goals) > 0, "goals not specified"

    cmd = ["mvn", "-B"] + goals
    return shell_runner.execute(cmd, cwd=cwd)


def print_error(execution_result: ExecutionResult, print_fn=print):
    for line in execution_result.stdout:
        if line.startswith("[ERROR]"):
            print_fn(f"{Colours.FAIL}{line}{Colours.ENDC}")
