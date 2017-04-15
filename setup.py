import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('withings_cli/cli.py', 'rb') as f:
    __version__ = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name="withings_cli",
    author="Kim Blomqvist",
    author_email="kblomqvist@iki.fi",
    version=__version__,
    description="A Command-line interface for Withings API",
    keywords=["withings", "cli-utilities"],
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "pytoml",
        "requests_oauthlib",
    ],
    entry_points='''
        [console_scripts]
        withings=withings_cli.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    url="https://github.com/kblomqvist/withings_cli",
    #download_url="https://github.com/kblomqvist/withings_cli/tarball/" + __version__,
)