import os

import git
from git import Repo

from ScriptConfig import ScriptConfig


class ResourceHandlerGithub(object):
    script_config = ScriptConfig()
    fetch_all = "git fetch --all"
    reset_hard = "git reset --hard"

    def download_scripts(self):
        destination = self.script_config.get_location()
        has_directory = self.check_if_directory_exists(destination)
        if has_directory:
            path = os.getcwd()
            os.chdir(destination)
            self.execute_cmd(self.fetch_all)
            self.execute_cmd(self.reset_hard)
            os.chdir(path)
        else:
            Repo.clone_from(self.get_repository(), destination)

    def check_if_directory_exists(self, destination):
        return os.path.exists(destination)

    def execute_cmd(self, command):
        cmd = git.cmd.Git()
        cmd.execute(command)

    def get_repository(self):
        repository = "https://github.com/triplejingle/OSRSPB"
        return repository
