import click
from awcrud.config import VERSION

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return  
    
    click.echo(f"Version {VERSION}")
    ctx.exit()