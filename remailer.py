import os
import requests

import click

""" CLI tool to install and un/set cron jobs. Cron jobs use `crontab` and run commands from `cron.py`. """


DEFAULT_CREDENTIALS="/home/jeadie/.fb-remailer"

def check_access_token(token) -> bool:
    """ Checks whether the access token is valid.

    Args:
        token: An Facebook access token

    Returns:
        True if the access token can access the `/me` endpoint, False otherwise. 
    """ 
    # TODO: Not great way to do it. Checks if access token only has access to jeadie. (i.e. not scale to more than one user).
    return requests.get(f"https://graph.facebook.com/me?access_token={token}").status_code == 200
    
def get_access_token() -> str:
    """ Gets the access token for Facebook.
    
    Finds an access token in the following order:
     * Checks the environment variable: FB_ACCESS_TOKEN
     * Checks whether the file DEFAULT_CREDENTIALS.token has a valid access token.
     * Checks whether the file DEFAULT_CREDENTIALS has a valid App ID and App Secret.
     * Returns None.

    Returns: An access token for the facebook account. If no access token could be found, returns None. 
    """
    if os.environ["FB_ACCESS_TOKEN"]:
        return os.environ["FB_ACCESS_TOKEN"]
    
    with open(f"{DEFAULT_CREDENTIALS}.token", "r") as token_file:
        access_token = token_file.read()
        if check_access_token(access_token):
            return access_token
    
    login(None, DEFAULT_CREDENTIALS)
    if os.environ["FB_ACCESS_TOKEN"]:
        return os.environ["FB_ACCESS_TOKEN"]
    return None


@click.group()
@click.pass_context
def remailer(ctx):
    ctx.ensure_object(dict)


@remailer.command(help="Stores an access token to file, given a FB app credentials and sets the environment variables: FB_ACCESS_TOKEN.")
@click.pass_context
@click.option('--credentials', default=DEFAULT_CREDENTIALS, help="File containing the Facebook App ID and Secret delimetered by a `,`.")
def login(ctx, credentials) -> int:
    try:    
        with open(credentials, "r") as f:
            app_id, app_secret =  f.read().strip("\n").split(",", 1)
    except FileNotFoundError as e:
        print(
            f"Failed to open FB credentials file. Error: {e}."
        )
        return 1
    except ValueError:
        print(
            f"{credentials} did not contain valid ID and secret delimetered by a `,`."
        )
        return 2

    access_token_resp = requests.get(
            "https://graph.facebook.com/oauth/access_token",
            params= {
                "client_id": app_id,
                "client_secret": app_secret,
                "grant_type": "client_credentials"
            }
        ).json()
    app_access_token =  access_token_resp["access_token"]

    with open(f"{credentials}.token", "w") as f:
        f.write(app_access_token)

    os.environ["FB_ACCESS_TOKEN"] = app_access_token
    return 0

if __name__ == '__main__':
    remailer(obj={})


# CLI tool
    # Get Notifications
    # Get events    