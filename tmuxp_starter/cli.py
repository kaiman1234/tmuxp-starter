import os
import pathlib
import typing as t

import click
from click import Context, Parameter, ParamType
from click.shell_completion import CompletionItem


class SessionType(ParamType):
    name = "session"

    def shell_complete(
        self, ctx: Context, param: Parameter, incomplete: str
    ) -> t.List["CompletionItem"]:

        session_path = pathlib.Path("~/.tmuxp").expanduser()
        sessions = set([
            session.stem
            for pattern in ["*.yaml", "*.yml", "*.json"]
            for session in session_path.glob(pattern)
        ])
        return [
            CompletionItem(session)
            for session in sessions
            if session.startswith(incomplete) or incomplete in session
        ]


@click.command()
@click.option("-d", "--detach", is_flag=True)
@click.argument("session", type=SessionType())
def main(detach, session):
    if detach:
        click.echo(f"Loading session {session} detached...")
        args = ["tmuxp", "load", "-y", "-d", session]
    else:
        click.echo(f"Loading session {session}...")
        args = ["tmuxp", "load", "-y", session]

    os.execvp("tmuxp", args)
