#!/usr/bin/env python2.5

# Make sure the user has setuptools installed!
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
    name = "pyke",
    version = "0.1.alpha1",
    packages = ['pyke', 'pyke.compiler'],
    package_data = {'pyke.compiler': ['*.krb']},

    install_requires = ['ply>=2.3'],
    extras_require = {
        'regen_docs': ["rest2web>=0.5"],
    },
    dependency_links = ['http://www.dabeaz.com/ply/'],

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
        "http://downloads.sourceforge.net/pyke/pyke-0.1.alpha1-py2.5.egg?modtime=1194563824&big_mirror=0",
    classifiers = [
        "Development Status :: 3 - Alpha",
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
