from pre_commit_maven.maven_checkstyle import main


def test_integration_given_good_example_and_invoke_checkstyle_then_return_0(
    temp_git_dir_with_resource
):
    cwd = temp_git_dir_with_resource("goodexample_checkstyle")

    assert main(cwd) == 0


def test_integration_given_bad_example_and_invoke_checkstyle_then_return_1(
    temp_git_dir_with_resource
):
    cwd = temp_git_dir_with_resource("badexample_checkstyle_fails")

    assert main(cwd) == 1
