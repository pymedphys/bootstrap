import typer
import click_spinner
import time

app = typer.Typer()


@app.command()
def main():
    print("Add in a dummy spinner because this installer isn't doing anything yet...")
    with click_spinner.spinner():
        time.sleep(5)


if __name__ == "__main__":
    app()
