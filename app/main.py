import os

from dotenv import load_dotenv
from slack_bolt import App

load_dotenv()


def get_slack_bolt_app():
    """
    Returns slack bolt app object after initializing.
    :return: Slack bolt app object
    """
    return App(
        token=os.getenv("SLACK_BOT_TOKEN"),
        signing_secret=os.getenv("SLACK_SIGNING_SECRET")
    )
