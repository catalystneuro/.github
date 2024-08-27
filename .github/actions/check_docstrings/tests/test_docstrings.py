import inspect
import pytest

def test_has_docstring(obj):
    """Check if an object has a docstring."""
    doc = inspect.getdoc(obj)
    if inspect.ismodule(obj):
        msg = f"{obj.__name__} has no docstring."
    else:
        msg = f"{obj.__module__}.{obj.__qualname__} has no docstring."
    assert doc is not None, msg
