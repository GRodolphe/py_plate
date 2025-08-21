"""Tests for the CLI module."""

from typer.testing import CliRunner

from py_plate import __version__
from py_plate.cli import app

runner = CliRunner()


def test_version() -> None:
    """Test version command."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_hello_default() -> None:
    """Test hello command with default parameters."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout


def test_hello_with_name() -> None:
    """Test hello command with custom name."""
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice!" in result.stdout


def test_hello_with_count() -> None:
    """Test hello command with count option."""
    result = runner.invoke(app, ["hello", "Bob", "--count", "2"])
    assert result.exit_code == 0
    output_lines = [line for line in result.stdout.split("\n") if "Hello Bob!" in line]
    assert len(output_lines) == 2


def test_hello_with_shout() -> None:
    """Test hello command with shout option."""
    result = runner.invoke(app, ["hello", "Charlie", "--shout"])
    assert result.exit_code == 0
    assert "HELLO CHARLIE!" in result.stdout


def test_info_command() -> None:
    """Test info command."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "System Information" in result.stdout
    assert "Python Version" in result.stdout
    assert "py_plate Version" in result.stdout


def test_config_show() -> None:
    """Test config show command."""
    result = runner.invoke(app, ["config", "--show"])
    assert result.exit_code == 0
    assert "Configuration:" in result.stdout
    assert "Debug:" in result.stdout


def test_config_set() -> None:
    """Test config set command."""
    result = runner.invoke(app, ["config", "--set", "debug", "true"])
    assert result.exit_code == 0
    assert "Set debug = true" in result.stdout


def test_config_set_without_value() -> None:
    """Test config set command without value (should fail)."""
    result = runner.invoke(app, ["config", "--set", "debug"])
    assert result.exit_code == 1
    assert "Error:" in result.stdout
    assert "Value required" in result.stdout


def test_help() -> None:
    """Test help command."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "A modern Python CLI template" in result.stdout
