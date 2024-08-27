import pytest
from .traverse import traverse_package
from importlib import import_module

def pytest_addoption(parser):
    parser.addoption("--package", action="store")
    parser.addoption("--names-to-skip", action="store", default="")

def pytest_generate_tests(metafunc):
    package_name = metafunc.config.getoption("--package")
    names_to_skip = metafunc.config.getoption("--names-to-skip")
    names_to_skip = names_to_skip.split(",") if names_to_skip != "" else []
    package = import_module(package_name)
    objs = traverse_package(package, package_name, names_to_skip=names_to_skip)
    if "obj" in metafunc.fixturenames:
        metafunc.parametrize("obj", objs)