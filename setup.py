"""
Package that contains the ranking algorithms used by the EVote software (@2008-2022)
"""
import re
import ast
from setuptools import setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("human_security/__init__.py", "r") as f:
    version = str(ast.literal_eval(_version_re.search(f.read()).group(1)))

setup(
    name="human_security",
    version=version,
    url="https://github.com/mdipierro/human_security",
    license="BSD",
    author="Massimo Di Pierro",
    author_email="massimo.dipierro@gmail.com",
    maintainer="Massimo Di Pierro",
    maintainer_email="massimo.dipierro@gmail.com",
    description="Provides easy to use API the RSA and AES",
    long_description=__doc__,
    packages=["human_security"],
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
