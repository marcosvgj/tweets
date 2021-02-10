import pathlib
import pkg_resources
import setuptools


def requirements() -> map:
    with pathlib.Path("requirements.txt").open() as r:
        yield map(str, pkg_resources.parse_requirements(r))


setuptools.setup(
    name="tweets",
    version="1.0.0",
    url="https://github.com/marcosvgj/tweets",
    author="Marcos Vinicius",
    author_email="e.marcosvgj@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements(),
)
