from pre_commit_maven.utils import shell


def execute_goals(goals: list, cwd: str, shell_runner=shell):
    assert goals is not None and len(goals) > 0, "goals not specified"

    cmd = ["mvn"] + goals
    return shell_runner.execute(cmd, cwd=cwd)
