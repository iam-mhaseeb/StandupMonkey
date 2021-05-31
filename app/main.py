import os

from slack_bolt import App


def get_slack_bolt_app():
    """
    Returns slack bolt app object after initializing.
    :return: Slack bolt app object
    """
    return App(
        token=os.environ.get("SLACK_BOT_TOKEN"),
        signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
    )
