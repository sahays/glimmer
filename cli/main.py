import typer
from rich import print

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    Say hello to NAME.
    """
    print(f"Hello [bold green]{name}[/bold green]!")

@app.command()
def goodbye(name: str, formal: bool = False):
    """
    Say goodbye to NAME.
    """
    if formal:
        print(f"Goodbye [bold blue]{name}[/bold blue]. Have a good day.")
    else:
        print(f"Later, [bold yellow]{name}[/bold yellow]!")

if __name__ == "__main__":
    app()
