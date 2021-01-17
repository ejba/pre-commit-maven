import pytest

from pre_commit_maven.utils.maven import execute_goals
from pre_commit_maven.utils.shell import ExecutionResult


def test_given_empty_goals_then_throws_assertion_error():
    with pytest.raises(AssertionError) as e:
        execute_goals([], ".")


def test_given_none_goals_then_throws_assertion_error():
    with pytest.raises(AssertionError) as e:
        execute_goals(None, ".")


def test_given_goals_then_run_maven(mocker):
    # given
    shell_runner = mocker.patch("pre_commit_maven.utils.shell")
    shell_runner.execute.return_value = ExecutionResult(0, "", "")

    # when
    execute_goals(["clean"], ".", shell_runner)

    # then
    shell_runner.execute.assert_called_once_with(["mvn", "-B", "clean"], cwd=".")
