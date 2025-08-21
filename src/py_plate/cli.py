"""Main CLI application using Typer."""

import platform
import sys
from typing import Annotated, Optional

import typer
from rich import print as rich_print
from rich.console import Console
from rich.table import Table

from py_plate import __version__

app = typer.Typer(
    name="py_plate",
    help="A modern Python CLI template with best practices.",
    add_completion=False,
    rich_markup_mode="rich",
)
console = Console()


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        rich_print(
            f"[bold green]py_plate[/bold green] version: [bold]{__version__}[/bold]"
        )
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            callback=version_callback,
            is_eager=True,
            help="Show version and exit.",
        ),
    ] = None,
) -> None:
    """Main entry point for the CLI."""


@app.command()
def hello(
    name: Annotated[str, typer.Argument(help="Name to greet")] = "World",
    count: Annotated[
        int, typer.Option("--count", "-c", help="Number of greetings")
    ] = 1,
    shout: Annotated[bool, typer.Option("--shout", help="Shout the greeting")] = False,
) -> None:
    """Greet someone with a friendly message."""
    greeting = f"Hello {name}!"
    if shout:
        greeting = greeting.upper()

    for _ in range(count):
        if shout:
            rich_print(f"[bold red]{greeting}[/bold red]")
        else:
            rich_print(f"[green]{greeting}[/green]")


@app.command()
def info() -> None:
    """Show system information."""
    table = Table(title="System Information")
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Python Version", sys.version.split()[0])
    table.add_row("Platform", platform.platform())
    table.add_row("Architecture", platform.architecture()[0])
    table.add_row("py_plate Version", __version__)

    console.print(table)


@app.command()
def config(
    show: Annotated[
        bool, typer.Option("--show", help="Show current configuration")
    ] = False,
    set_key: Annotated[
        Optional[str], typer.Option("--set", help="Set configuration key")
    ] = None,
    value: Annotated[Optional[str], typer.Argument(help="Configuration value")] = None,
) -> None:
    """Manage application configuration."""
    if show:
        rich_print("[bold blue]Configuration:[/bold blue]")
        rich_print("  • Debug: [green]False[/green]")
        rich_print("  • Verbose: [green]False[/green]")
        rich_print("  • Output Format: [yellow]json[/yellow]")
        return

    if set_key and value:
        rich_print(
            f"[green]Set[/green] [cyan]{set_key}[/cyan] = [yellow]{value}[/yellow]"
        )
        return

    if set_key and not value:
        rich_print("[red]Error:[/red] Value required when setting configuration")
        raise typer.Exit(1)

    rich_print(
        "Use [cyan]--show[/cyan] to view configuration or [cyan]--set KEY VALUE[/cyan] to set values"
    )


if __name__ == "__main__":
    app()
