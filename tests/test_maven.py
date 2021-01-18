import pytest
from pre_commit_maven.maven import main


def test_given_none_goals_then_throws_assertion_error():
    with pytest.raises(SystemExit) as e:
        main([], ".")


def test_given_goals_then_executes_generic_main(mocker):
    mocked_execute_fn = mocker.Mock()

    main(["test"], ".", execute_fn=mocked_execute_fn)

    mocked_execute_fn.assert_called_once_with(["test"], ".")
