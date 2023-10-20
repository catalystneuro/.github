import pytest
from .traverse import traverse_package
from importlib import import_module

def pytest_addoption(parser):
    parser.addoption("--package", action="store")

def pytest_generate_tests(metafunc):
    package_name = metafunc.config.getoption("--package")
    package = import_module(package_name)
    objs = traverse_package(package, package_name)
    if "obj" in metafunc.fixturenames:
        metafunc.parametrize("obj", objs)