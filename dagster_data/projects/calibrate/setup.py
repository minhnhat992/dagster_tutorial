import setuptools

setuptools.setup(
    name="calibrate",
    packages=setuptools.find_packages(exclude=["calibrate_tests"]),
    install_requires=[
        "dagster==0.12.11",
        "dagit==0.12.11",
        "pytest",
    ],
)
