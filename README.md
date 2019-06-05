# Python Project Creator

## About
This project was created for a better workflow when creating new projects


from setuptools import setup

setup(
    name='Python Project Creator',
    version='1.0',
    packages=['Create'],
    url='',
    license='',
    author='Rick Venema',
    author_email='',
    description='A Python Project Creator',
    scripts=['Create/create.py',
             'Create/README-Template.md'],
    entry_points={
        'console_scripts': [
            'create=Create.__main__:main'
        ],
    }, install_requires=['Create']
)
