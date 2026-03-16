"""Unit tests for secureflow-detect core modules."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_imports():
    """Test that core modules can be imported."""
    from secureflow_detect.core import settings
    from secureflow_detect.core import enums
    assert settings is not None
    assert enums is not None


def test_trailsdict_basic():
    """Test TrailsDict basic operations."""
    from secureflow_detect.core.trailsdict import TrailsDict
    td = TrailsDict()
    assert isinstance(td, dict)


def test_addr_to_int():
    """Test IP address to integer conversion."""
    from secureflow_detect.core.addr import addr_to_int
    result = addr_to_int("192.168.1.1")
    assert isinstance(result, int)
    assert result > 0


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
