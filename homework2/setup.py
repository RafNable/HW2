from setuptools import find_packages, setup

setup(
    name="homework2",
    packages=find_packages(exclude=["homework2_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
