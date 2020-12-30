import click

""" CLI tool for `crontab` to use. """
#TODO: just do this in Bash

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cron(ctx, debug):
    
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug

@cron.command()
@click.pass_context
@click.option('--timeout', default=8000, help="You ain't getting help.")
def sync(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))

if __name__ == '__main__':
    cron(obj={})
