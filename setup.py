#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "pyke",
    version = "1.1.1",
    packages = ['pyke', 'pyke.krb_compiler', 'pyke.krb_compiler.ply'],
    package_data = {
        'pyke.krb_compiler': ['*.krb'],
        'pyke.krb_compiler.ply': ['README', 'README.pyke'],
    },

    # old setuptools stuff:
    #install_requires = [],
    #extras_require = {
    #    'regen_docs': ["rest2web>=0.5"],
    #    'examples': ["HTMLTemplate>=1.5"],
    #    'tests': ["doctest-tools>=1.0a3"],
    #},
    #zip_safe = True,

    # Metadata for upload to PyPI
    author = "Bruce Frederiksen",
    author_email = "dangyogi@gmail.com",
    description = "Python Knowledge Engine and Automatic Python Program Generator",
    license = "MIT License",
    keywords = "expert system forward backward chaining backtracking plans",
    url = "http://sourceforge.net/projects/pyke",
    long_description = """
        Both forward-chaining and backward-chaining rules (which may include
        python code) are compiled into python. Can also automatically assemble
        python programs out of python functions which are attached to
        backward-chaining rules.
    """,
    download_url =
        "http://downloads.sourceforge.net/pyke/pyke-1.1.1.zip",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: Log Analysis",
    ],
)
