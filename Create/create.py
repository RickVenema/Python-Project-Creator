"""

"""

import argparse


class Create:
    def __init__(self):
        self.arguments = self.argparser_create()

    @staticmethod
    def argparser_create():
        parser = argparse.ArgumentParser(description="Tool for creating new python projects")
        parser.add_argument("--git", "-g", default=True, help="Initialize with git repository")
        args = parser.parse_args()
        return args


if __name__ == '__main__':
    create = Create()