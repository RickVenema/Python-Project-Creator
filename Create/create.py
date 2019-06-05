"""

"""

import argparse
import os


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
        args = parser.parse_args()
        return args

    def create_directory(self, name):
        os.mkdir(self.path + "/" + name)

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

        print("jumped")


if __name__ == '__main__':
    create = Create()
