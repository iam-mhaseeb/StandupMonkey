import os

from slack_bolt import App

from wsgi import app


def get_slack_bolt_app():
    """
    Returns slack bolt app object after initializing.
    :return: Slack bolt app object
    """
    return App(
        token=os.environ.get("SLACK_BOT_TOKEN"),
        signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
    )


@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")
