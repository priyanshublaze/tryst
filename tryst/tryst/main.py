import typer
import time
from datetime import date


app = typer.Typer()
wfile = ""
user = "user"


@app.command()
def create(filename: str = typer.Argument(..., help="Name of Python file to be created"),
           modules: str = typer.Option(..., "--mod", "-mod", prompt="Enter all the required modules(separated by commas)",
                                       help="List all the required Python modules"),
           out: str = typer.Option(False, "--out", "-out", help="set True if you want output block")):
    """
    Creates a boilerplate code along with importing all the required Modules.
    Example: tryst create hello-world --out
    """
    typer.secho(f"Creating file {filename}.py ...",
                fg=typer.colors.GREEN, bold=True)
    file_nm = filename+".py"
    day = date.today()
    global wfile
    wfile = open(file_nm, "a")
    wfile.write(f"#Program created by {user} on {day}\n\n")
    if modules != "none":
        for i in modules.split(","):
            wfile.write(f"import {i.lower()}\n")
    wfile.write("\n\n")
    wfile.write("def main(parameter):\n  pass\n\n\n")
    wfile.write('if __name__ == "__main__":\n  pass\n\n\n')
    if out == True:
        wfile.write('"""\nOUTPUT:\n\n"""')


@app.command()
def inject(dat: typer.FileText = typer.Option(..., "-dat", "-d"), config: typer.FileTextWrite = typer.Option(..., "-config", "-c", mode="a")):
    """
    Injects a comment/code block at the end of a file
    """
    try:
        typer.secho("Initializing Injection...",
                    fg=typer.colors.BRIGHT_CYAN)
        time.sleep(0.8)
        typer.secho("Reading files...", fg=typer.colors.CYAN)
        time.sleep(1.0)
        num = 0
        for line in dat:
            n = config.write(line)
            num += n
            time.sleep(0.6)
        config.write("\n\n")

        with typer.progressbar(range(100), label="Processing") as progress:
            for value in progress:
                time.sleep(0.01)
        typer.echo(f"Processed {num} letters.")
        typer.secho("Injection Status: SUCCESS",
                    fg=typer.colors.BRIGHT_GREEN, bold=True)
    except:
        typer.secho("Injection Status: FAILED",
                    fg=typer.colors.BRIGHT_RED, bold=True, err=True)
        typer.echo("Some unknown error occured.")
        typer.Abort()


@app.command()
def chuser(usr: str = typer.Argument(..., help="Enter your name as you want in your code")):
    """
    Change the global user
    """
    global user
    user = usr
