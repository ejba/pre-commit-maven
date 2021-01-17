import pytest
from pytest_mock import MockerFixture
from pre_commit_maven.utils.maven import execute
from pre_commit_maven.utils.maven import print_error
from pre_commit_maven.utils.maven import Colours
from pre_commit_maven.utils.shell import ExecutionResult

MAVEN_OPTS = "-client -XX:+TieredCompilation -XX:TieredStopAtLevel=1 -Xverify:none"


def test_given_empty_goals_then_throws_assertion_error():
    with pytest.raises(AssertionError) as e:
        execute([], ".")


def test_given_none_goals_then_throws_assertion_error():
    with pytest.raises(AssertionError) as e:
        execute(None, ".")


def test_given_goals_then_run_maven(mocker):
    # given
    shell_runner = mocker.patch("pre_commit_maven.utils.shell")
    shell_runner.exists_file.return_value = False
    shell_runner.execute.return_value = ExecutionResult(0, "", "")

    # when
    execute(["clean"], ".", shell_runner, {})

    # then
    shell_runner.exists_file.assert_called_once_with("./mvnw")
    shell_runner.execute.assert_called_once_with(
        ["mvn", "--batch-mode", "clean"], cwd=".", env={"MAVEN_OPTS": MAVEN_OPTS}
    )


def test_given_mvnw_exists_then_run_mvnw(mocker):
    # given
    shell_runner = mocker.patch("pre_commit_maven.utils.shell")
    shell_runner.exists_file.return_value = True
    shell_runner.execute.return_value = ExecutionResult(0, "", "")

    # when
    execute(["clean"], ".", shell_runner, {})

    # then
    shell_runner.exists_file.assert_called_once_with("./mvnw")
    shell_runner.execute.assert_called_once_with(
        ["./mvnw", "--batch-mode", "clean"], cwd=".", env={"MAVEN_OPTS": MAVEN_OPTS}
    )


def test_given_stdout_without_error_log_then_prints_nothing(mocker):
    # given
    mocked_print = mocker.Mock()
    execution_result = ExecutionResult(0, "[INFO] Stuffs", "")

    # when
    print_error(execution_result, mocked_print)

    # then
    assert not mocked_print.called


def test_given_stdout_with_error_log_then_prints_error_log(mocker: MockerFixture):
    # given
    mocked_print = mocker.Mock()

    stdout = "[ERROR] Tests run: 1, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0.007 s <<< FAILURE! - in com.badexample.AppTest"
    execution_result = ExecutionResult(0, stdout, "")

    # when
    print_error(execution_result, mocked_print)

    # then
    mocked_print.assert_called_once_with(f"{Colours.FAIL}{stdout}{Colours.ENDC}")
