from pre_commit_maven.maven_goals import main


def test_integration_given_bad_example_and_invoke_spotless_then_return_1(
    temp_git_dir_with_resource
):
    cwd = temp_git_dir_with_resource("badexample")

    assert main(["spotless:check"], cwd) == 1


def test_integration_given_good_example_and_invoke_spotless_then_return_0(
    temp_git_dir_with_resource
):
    cwd = temp_git_dir_with_resource("goodexample")

    assert main(["spotless:check"], cwd) == 0


def test_integration_given_bad_example_and_invoke_clean_then_return_0(
    temp_git_dir_with_resource
):
    cwd = temp_git_dir_with_resource("badexample")

    assert main(["clean"], cwd) == 0
