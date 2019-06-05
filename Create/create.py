"""

"""

import argparse
import os
import time
import subprocess


class Create:
    def __init__(self):
        self.path = os.getcwd()
        self.arguments = self.argparser_create()
        self.run()

    @staticmethod
    def argparser_create():
        parser = argparse.ArgumentParser(description="Tool for creating new python projects")
        parser.add_argument("--folder_name", "-f", help="The folder name of the project", dest="folder_name")
        parser.add_argument("--git", "-g",  action='store_true',
                            help="Initialize with git repository", dest="git")
        parser.add_argument("--README", "-r", action='store_true',
                            help="Initialize with README", dest="README")
        args = parser.parse_args()
        return args

    def create_directory(self, name):
        os.mkdir(self.path + "/" + name)

    def create_readme(self):
        f = open(self.path + "/" + self.arguments.folder_name + "/" + "README.md", "w+")
        f.close()

    def init_git(self):
        subprocess.run("git init " + self.arguments.folder_name)
        # subprocess.run("cd " + self.arguments.folder_name + "/")

    def run(self):
        try:
            if self.arguments.folder_name:
                self.create_directory(self.arguments.folder_name)
            else:
                raise NotADirectoryError("Folder not specified")
        except NotADirectoryError:
            print("Folder not specified")
            print("use --help (or -h) for more information about the arguments")
            exit()

        if self.arguments.README:
            self.create_readme()

        if self.arguments.git:
            self.init_git()


if __name__ == '__main__':
    create = Create()
