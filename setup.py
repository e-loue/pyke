#!/usr/bin/env python2.5

# Make sure the user has setuptools installed!
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
    name = "pyke",
    version = "0.6",
    packages = ['pyke', 'pyke.krb_compiler'],
    package_data = {'pyke.krb_compiler': ['*.krb']},

    install_requires = ['ply>=2.5'],
    extras_require = {
        'regen_docs': ["rest2web>=0.5"],
        'examples': ["HTMLTemplate>=1.5"],
    },

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
        "http://downloads.sourceforge.net/pyke/pyke-0.6-py2.5.egg",
    classifiers = [
        "Development Status :: 4 - Beta",
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
