import os
import click
import pathlib


def get_sessions(ctx, args, incomplete):
    path = pathlib.Path("~/.tmuxp").expanduser()
    sessions = [
        (p.stem, str(p)) for p in path.glob("*.yaml")
    ]
    return [s for s in sessions if incomplete in s[0]]


@click.command()
@click.option("-d", "--detach", is_flag=True)
@click.argument("session", type=click.STRING, autocompletion=get_sessions)
def main(detach, session):
    if detach:
        click.echo(f"Loading session {session} detached...")
        args = ["tmuxp", "load", "-y", "-d", session]
    else:
        click.echo(f"Loading session {session}...")
        args = ["tmuxp", "load", "-y", session]

    os.execvp("tmuxp", args)
