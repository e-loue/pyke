# setup.py

# Packages CanNotProve test into egg file.

from setuptools import setup

setup(
    name = "CanNotProve",
    version = "1.0.1",
    packages = ['CanNotProve', 'CanNotProve.compiled_krb'],
    package_data = {
        'CanNotProve': ['facts.kfb', 'rules.krb'],
        'CanNotProve.compiled_krb': ['facts.fbc'],
    },
    zip_safe = True,
)
