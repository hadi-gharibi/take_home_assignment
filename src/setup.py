import os
from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))

setup(
    name="mypack",
    version="0.0.1",
    # Author details
    author="<Add your name>",
    author_email="<Add your email address>",
    # Choose your license
    license="All Rights Reserved",
    #package_dir={"": "main"},
    packages = find_packages(include='tests'),
    entry_points={"console_scripts": ["db_import=assignment.main:main"]},
    install_requires=[
        "psycopg2==2.8.6",
        "python-dateutil",
        "SQLAlchemy"
    ],
    tests_require=[
        "pytest",
    ],
)