"""Pytest configuration and fixtures."""

from pathlib import Path

import pytest


@pytest.fixture  # type: ignore[misc]
def sample_data() -> dict[str, str]:
    """Sample data fixture for tests."""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "role": "admin",
    }


@pytest.fixture  # type: ignore[misc]
def temp_config_file(tmp_path: Path) -> Path:
    """Create a temporary configuration file for testing."""
    config_file = tmp_path / "config.json"
    config_file.write_text('{"debug": false, "verbose": true}')
    return config_file
