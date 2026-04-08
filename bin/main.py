import click
from awcrud.core import *

@click.command()
@click.option('-v', '--version', callback=print_version, is_eager=True, is_flag=True, help='Returns the current software version.')

def cli(version):
    pass  

if __name__ == '__main__':
    cli()