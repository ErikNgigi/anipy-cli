from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='anipy_cli',
    packages=find_packages(include=['anipy_cli']),
    version='2.0.2',
    description='Little tool in python to watch anime from the terminal (the better way to watch anime)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='sdaqo',
    author_email='sdaqo.dev@protonmail.com',
    url='https://github.com/sdaqo/anipy-cli',
    license='GPL-3.0',
    install_requires=['bs4', 'requests', 'tqdm', 'pycryptodomex'],
    entry_points="[console_scripts]\nanipy-cli=anipy_cli.cli:main",
)
