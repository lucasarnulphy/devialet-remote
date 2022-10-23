import typer
import list
import action
import listener

app = typer.Typer()
app.add_typer(list.app, name="list")
app.add_typer(action.app, name="action")
app.add_typer(listener.app, name="listener")

if __name__ == "__main__":
    app()