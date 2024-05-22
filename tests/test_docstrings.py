import inspect
import pytest

def test_has_docstring(obj):
    """Check if an object has a docstring."""
    if inspect.ismodule(obj):
        return # modules do not require docstrings
    
    doc = inspect.getdoc(obj)
    msg = f"{obj.__module__}.{obj.__qualname__} has no docstring."
    assert doc is not None, msg
