import pytest


@pytest.fixture(scope="module")
def model():
    """Create a model object that will also serve as the root directory for all
    other model elements"""
    model = sysml.Model("NCC-1701")
    return model