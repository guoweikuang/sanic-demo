import click
from tortoise import run_async
from tortoise import Tortoise
from tortoise.exceptions import IntegrityError

from db import init_db
from models.user import create_user


async def init():
    await init_db(create_db=True)
    await Tortoise.generate_schemas()


@click.group()
def cli():
    ...


@cli.command()
def initdb():
    run_async(init())
    click.echo("Init Database Finished!")


async def _adduser(name, email, password):
    await init_db()
    try:
        user = await create_user(name=name, email=email, password=password)
    except IntegrityError as e:
        click.echo(str(e))
    else:
        click.echo(f"User {user.username} created, ID: {user.id}")


@cli.command()
@click.option('--name', required=True, prompt=True)
@click.option('--email', required=False, default=None, prompt=True)
@click.option('--password', required=True, prompt=True,
              hide_input=True, confirmation_prompt=True)
def adduser(name, email, password):
    run_async(_adduser(name=name, email=email, password=password))


if __name__ == '__main__':
    cli()