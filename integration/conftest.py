import pytest
import shutil
import os.path

from pre_commit_maven.utils import shell
from integration.utils import get_resource_path


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join("gits")
    shell.execute(["git", "init", "--", str(git_dir)])
    yield git_dir


@pytest.fixture
def temp_git_dir_with_resource(temp_git_dir):
    def _copy_project_to_git_dir(resource):
        resource_path = get_resource_path(resource)
        project_path = os.path.join(temp_git_dir, resource)
        shutil.copytree(resource_path, project_path)
        return project_path

    return _copy_project_to_git_dir
