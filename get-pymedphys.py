import typer
import click_spinner
import time

app = typer.Typer()


@app.command()
def main():
    with click_spinner.spinner():
        time.sleep(1)
    
    raise ValueError("Boo")
    

if __name__ == "__main__":
    app()
