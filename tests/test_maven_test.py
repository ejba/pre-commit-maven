import pytest
from pre_commit_maven.maven_test import main


def test_given_goals_then_executes_generic_main(mocker):
    mocked_execute_fn = mocker.Mock()

    main(".", execute_fn=mocked_execute_fn)

    mocked_execute_fn.assert_called_once_with(["clean", "test"], ".")
